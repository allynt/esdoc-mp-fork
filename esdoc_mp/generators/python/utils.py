# -*- coding: utf-8 -*-

"""Encapsualtes a set of python specific name conversion operations.

"""
from esdoc_mp.generators.generator_utils import *



# Language name constant.
LANGUAGE = 'python'

# Language prefix constant.
LANGUAGE_PREFIX = 'py'

# Language file extension constant.
FILE_EXTENSION = '.py'

# Python package initialisation file name.
_PACKAGE_INIT_FILE = '__init__'

# Python clas property field prefix.
_PROPERTY_FIELD_PREFIX = 'self.'

# Set of simple type mappings.
_SIMPLE_TYPE_MAPPINGS = {
    'bool' : 'bool',
    'date' : 'datetime.date',
    'datetime' : 'datetime.datetime',
    'float' : 'float',
    'int' : 'int',
    'str' : 'unicode',
    'unicode' : 'unicode',
    'uri' : 'unicode',
    'uuid' : 'uuid.UUID',
}

# Standard null value.
_NULL_VALUE = 'None'

# Iterable null value.
_NULL_VALUE_ITERABLE = '[]'


def _strip(name):
    """Returns stripped name.

    Keyword Arguments:
    name - name being converted.

    """
    if isinstance(name, str) == False:
        name = name.name
    return name


def _strip_class_name(name):
    """Returns stripped class name.

    Keyword Arguments:
    name - name being converted.

    """
    name = _strip(name)
    if name.find('.') != -1:
        name = name.split('.')[len(name.split('.')) - 1]
    return name


def get_ontology_name(name):
    """Converts name to a python ontology name.

    Keyword Arguments:
    name - name being converted.

    """
    if isinstance(name, str) == False:
        name = name.name

    return name.lower()


def get_ontology_version(name):
    """Converts version identifier to a python ontology version.

    Keyword Arguments:
    name - name of version identifier being converted.

    """
    if isinstance(name, str) == False:
        name = name.version

    return name.replace(".", "_")


def _get_ontology_directory(o, root=None, sub=None, suffix_root=False):
    """Returns ontology directory into which code is generated code.

    Keyword Arguments:
    ontology - ontology being processed.
    root - root directory with which ontology is associated.
    sub - sub directory to append as a suffix.
    suffix_root_dir - flag indicating whether to append a standard suffix to root directory.

    """
    dir = ''
    if root is not None:
        dir += root + '/'
    if suffix_root == True:
        dir += 'cim_codegen/python/'
        dir += get_ontology_name(o)
    dir += get_ontology_name(o)
    dir += '/'
    dir += 'v' + get_ontology_version(o)
    if sub is not None:
        dir += '/' + sub
    return dir


def get_ontology_directory(ctx, sub=None, include_version=True):
    """Returns ontology directory into which code is generated code.

    :param GeneratorContext ctx: Generation context information.
    :param str sub: Subpackage name.
    :param bool include_version: Subpackage name.

    """
    dir = ''
    if ctx.output_dir is not None:
        dir += ctx.output_dir + '/'
    dir += get_ontology_name(ctx.ontology)
    if include_version:
        dir += '/'
        dir += 'v' + get_ontology_version(ctx.ontology)
    if sub is not None:
        dir += '/'
        dir += sub

    return dir


def get_package_name(name):
    """Converts name to a python package name.

    :param str name: Package name being converted.

    """
    return _strip_package_name(name)


def get_full_class_name(c):
    """Converts name to a python class name.

    :param str name: Class name being converted.

    """
    return get_package_name(c.package) + "." + get_class_name(c)


def get_class_name(name):
    """Converts name to a python class name.

    :param str name: Class name being converted.

    """
    return convert_to_camel_case(_strip_class_name(name))


def get_class_import_name(name):
    """Converts name to a python class import name.

    :param str name: Class name being converted.

    """
    return _strip_class_name(name)


def get_class_functional_name(name):
    """Converts name to one suitable for use in a python function definition.

    :param str name: Class name being converted.

    """
    return _strip_class_name(name)


def get_class_doc_string_name(name):
    """Converts name to one suitable for use in python documentation.

    :param str name: Class name being converted.

    """
    name = _strip_class_name(name)
    return name.replace('_', ' ')


def _get_class_file_name(name):
    """Converts name to a python class file name.

    :param str name: Class name being converted.

    """
    name = _strip_class_name(name)
    return name + FILE_EXTENSION


def _get_class_base_name(c):
    """Converts name to a python base class name.

    """
    if c.base is None:
        return 'object'
    elif c.base.package == c.package:
        return get_class_name(c.base)
    else:
        return get_full_class_name(c.base)


def get_property_ctor(p):
    """Converts class property to a python property constructor declaration.

    """
    return 'self.{0} = {1}'.format(get_property_name(p),
                                   get_property_default_value(p))


def get_property_reference_ctor(p):
    """Converts class property to a python reference property constructor declaration.

    """
    return 'self.reference_to_{0} = {1}'.format(get_property_name(p), get_property_default_value(p))


def get_property_name(name):
    """Converts name to a python class property name.

    """
    return _strip(name)


def get_property_field_name(name):
    """Converts name to a python class property field name.

    """
    return _PROPERTY_FIELD_PREFIX + _strip(name)


def get_property_default_value(p):
    """Returns property default value.

    """
    # Return value based upon property type:
    # ... meta information;
    if p.name == "meta":
        if p.package == p.type.package:
            return "{0}()".format(get_type_name(p.type))
        else:
            return "{0}.{1}()".format(get_package_name(p.type.package),
                                      get_type_name(p.type))

    # ... iterative types;
    elif p.is_iterative:
        return _NULL_VALUE_ITERABLE

    # ... enum / complex / simple types.
    else:
        return _NULL_VALUE


def get_type_name(type):
    """Returns python type name.

    :param str name: Type name being converted.

    """
    name = type.name
    if type.is_simple:
        return _get_simple_type_mapping(name)
    elif type.is_enum:
        return _get_simple_type_mapping('unicode')
    elif type.is_complex:
        return get_class_name(name)


def get_type_functional_name(t, get_full_name=False):
    """Returns python type functional name.

    :param str name: Type name being converted.

    """
    name = t.name
    if t.is_simple:
        return _get_simple_type_mapping(name)
    elif t.is_enum:
        return 'unicode'
    elif t.is_complex:
        if get_full_name:
            return get_package_name(name) + "." + get_class_name(name)
        else:
            return get_class_name(name)


def get_type_doc_name(t):
    """Returns python type documentation name.

    :param str name: Type name being converted.

    """
    name = t.name
    if t.is_simple:
        return _get_simple_type_mapping(name)
    elif t.is_enum:
        return '{0}.{1}'.format(get_package_name(name), get_enum_name(name))
    elif t.is_complex:
        return '{0}.{1}'.format(get_package_name(name), get_class_name(name))


def _strip_enum_name(name):
    """Returns stripped enum name.

    """
    name = _strip(name)
    if name.find('.') != -1:
        name = name.split('.')[len(name.split('.')) - 1]
    return name


def get_enum_name(name):
    """Converts name to a python enum name.

    :param str name: Enum name being converted.

    """
    return convert_to_camel_case(_strip_enum_name(name))


def get_enum_file_name(name):
    """Converts name to a python enum file name.

    :param str name: Enum name being converted.

    """
    return _strip_enum_name(name) + FILE_EXTENSION


def _get_simple_type_mapping(simple):
    """Returns matching simple type mapping.

    """
    return _SIMPLE_TYPE_MAPPINGS[simple]


def _strip_package_name(name):
    """Returns stripped package name.

    """
    name = _strip(name)
    if name.find('.') != -1:
        name = name.split('.')[0]
    return name


def get_package_init_file_name():
    """Returns python package init file name.

    :param str name: Package name being converted.

    """
    return _PACKAGE_INIT_FILE + FILE_EXTENSION



def get_package_module_name(name, prefix):
    """Returns a package module name by injecting package name into a template.

    :param str name: Package name.
    :param str prefix: A package name prefix, e.g. "validator".

    """
    return (prefix + "_for_{0}_package").format(get_package_name(name))


def get_package_module_file_name(name, prefix):
    """Returns a package module file name by injecting package name into a template.

    :param str name: Package name.
    :param str prefix: A package name prefix, e.g. "validator".

    """
    return get_package_module_name(name, prefix) + FILE_EXTENSION


def get_module_file_name(name):
    """Returns a module file name.

    :param str name: Module name.

    """
    return name + FILE_EXTENSION


def format(o):
    """Pythonizes ontology names.

    """
    o.op_name = get_ontology_name(o)
    o.op_version = get_ontology_version(o)

    for p in o.packages:
        p.op_name = get_package_name(p)

    for c in o.classes:
        c.op_base_name = _get_class_base_name(c)
        c.op_doc_string_name = get_class_doc_string_name(c)
        c.op_file_name = _get_class_file_name(c)
        c.op_functional_name = get_class_functional_name(c)
        c.op_import_name = get_class_import_name(c)
        c.op_name = get_class_name(c)
        c.op_full_name = get_full_class_name(c)