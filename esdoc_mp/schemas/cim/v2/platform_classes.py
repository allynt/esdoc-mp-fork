# -*- coding: utf-8 -*-

"""
.. module:: platform_classes.py
   :synopsis: Set of CIM v2 ontology type definitions.

"""


def component_performance():
    """Describes the simulation rate of a component in seconds per model day.

    """
    return {
        'type': 'class',
        'base': None,
        'is_abstract': False,
        'pstr': ('speed %s s/day', ('speed',)),
        'properties': [
            ('component', 'software.software_component', '0.1',
                "Link to a CIM software component description."),
            ('component_name', 'str', '1.1',
                "Short name of component."),
            ('cores_used', 'int', '0.1',
                "Number of cores used for this component."),
            ('nodes_used', 'int', '0.1',
                "Number of nodes used for this component."),
            ('speed', 'float', '1.1',
                "Time taken to simulate one real day (s).")
        ]
    }


def compute_pool():
    """Homogeneous pool of nodes within a computing machine.

    """
    return {
        'type': 'class',
        'base': None,
        'is_abstract': False,
        'properties': [
            ('accelerator_type', 'str', '0.1',
                "Type of accelerator."),
            ('accelerators_per_node', 'int', '0.1',
                "Number of accelerator units on a node."),
            ('compute_cores_per_node', 'int', '0.1',
                "Number of CPU cores per node."),
            ('cpu_type', 'str', '0.1',
                "CPU type."),
            ('description', 'str', '0.1',
                "Textural description of pool."),
            ('interconnect', 'str', '0.1',
                "Interconnect used."),
            ('memory_per_node', 'platform.storage_volume', '0.1',
                "Memory per node."),
            ('model_number', 'str', '0.1',
                "Model/Board number/type."),
            ('name', 'str', '0.1',
                "Name of compute pool within a machine."),
            ('number_of_nodes', 'int', '0.1',
                "Number of nodes."),
            ('operating_system', 'str', '0.1',
                "Operating system.")
        ]
    }


def machine():
    """A computer/system/platform/machine which is used for simulation.

    """
    return {
        'type': 'class',
        'base': 'platform.partition',
        'is_abstract': False,
        'properties': [
            ('meta', 'shared.doc_meta_info', '1.1',
                "Document description.")
        ]
    }


def partition():
    """A major partition (component) of a computing system (aka machine).

    """
    return {
        'type': 'class',
        'base': None,
        'is_abstract': False,
        'properties': [
            ('compute_pools', 'platform.compute_pool', '1.N',
                "Layout of compute nodes."),
            ('description', 'str', '0.1',
                "Textural description of machine."),
            ('institution', 'linked_to(shared.party)', '1.1',
                "Institutional location."),
            ('model_number', 'str', '0.1',
                "Vendor's model number/name - if it exists."),
            ('name', 'str', '1.1',
                "Name of partition (or machine)."),
            ('online_documentation', 'shared.online_resource', '0.N',
                "Links to documentation."),
            ('partition', 'platform.partition', '0.N',
                "If machine is partitioned, treat subpartitions as machines."),
            ('storage_pools', 'platform.storage_pool', '0.N',
                "Storage resource available."),
            ('vendor', 'linked_to(shared.party)', '0.1',
                "The system integrator or vendor."),
            ('when_used', 'shared.time_period', '0.1',
                "If no longer in use, the time period it was in use.")
        ]
    }


def performance():
    """Describes the properties of a performance of a configured model on a particular system/machine.

    """
    return {
        'type': 'class',
        'base': None,
        'is_abstract': False,
        'pstr': ('%s (sypd:%s)', ('name', 'sypd')),
        'properties': [
            ('asypd', 'float', '0.1',
                "Actual simulated years per wall-clock day, all-in."),
            ('chsy', 'float', '0.1',
                "Core-Hours per simulated year."),
            ('compiler', 'str', '0.1',
                "Compiler used."),
            ('coupler_load', 'float', '0.1',
                "Percentage of time spent in coupler."),
            ('io_load', 'float', '0.1',
                "Percentage of time spent in I/O."),
            ('load_imbalance', 'float', '0.1',
                "Load imbalance."),
            ('memory_bloat', 'float', '0.1',
                "Percentage of extra memory needed."),
            ('meta', 'shared.doc_meta_info', '1.1',
                "Document metadata."),
            ('model', 'linked_to(science.model)', '1.1',
                "Model for which performance was tested."),
            ('name', 'str', '0.1',
                "Short name for performance (experiment/test/whatever)."),
            ('platform', 'linked_to(platform.machine)', '1.1',
                "Platform on which performance was tested."),
            ('subcomponent_performance', 'platform.component_performance', '0.1',
                "Describes the performance of each subcomponent."),
            ('sypd', 'float', '0.1',
                "Simulated years per wall-clock day."),
            ('total_nodes_used', 'int', '0.1',
                "Number of nodes used.")
        ]
    }


def storage_pool():
    """Homogeneous storage pool on a computing machine.

    """
    return {
        'type': 'class',
        'base': None,
        'is_abstract': False,
        'properties': [
            ('description', 'str', '0.1',
                "Description of the technology used."),
            ('name', 'str', '1.1',
                "Name of storage pool."),
            ('type', 'platform.storage_systems', '0.1',
                "Type of storage."),
            ('vendor', 'linked_to(shared.party)', '0.1',
                "Vendor of the storage unit."),
            ('volume_available', 'platform.storage_volume', '1.1',
                "Storage capacity.")
        ]
    }


def storage_systems():
    """Controlled vocabulary for storage  types (including filesystems).

    """
    return {
        'type': 'enum',
        'is_open': False,
        'members': [
            ("Lustre", None),
            ("GPFS", None),
            ("isilon", None),
            ("NFS", None),
            ("Panasas", None),
            ("Other Disk", None),
            ("Tape - MARS", None),
            ("Tape - MASS", None),
            ("Tape - Castor", None),
            ("Tape - Other", None),
            ("Unknown", None)
        ]
    }


def storage_volume():
    """Volume and units.

    """
    return {
        'type': 'class',
        'base': None,
        'is_abstract': False,
        'pstr': ('%s %s', ('volume', 'units')),
        'properties': [
            ('units', 'platform.volume_units', '1.1',
                "Volume units."),
            ('volume', 'int', '1.1',
                "Numeric value.")
        ]
    }


def volume_units():
    """Appropriate storage volume units.

    """
    return {
        'type': 'enum',
        'is_open': False,
        'members': [
            ("GB", "Gigabytes (1000^3)"),
            ("TB", "Terabytes (1000^4)"),
            ("PB", "Petabytes (1000^5)"),
            ("EB", "Exabytes (1000^6)"),
            ("TiB", "Tebibytes (1024^4)"),
            ("PiB", "Pebibytes (1024^5)"),
            ("EiB", "Exbibytes (1024^6)")
        ]
    }
