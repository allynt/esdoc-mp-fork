# -*- coding: utf-8 -*-

"""
.. module:: science_classes.py
   :synopsis: Set of CIM v2 ontology type definitions.

"""


def algorithm():
    """Used to hold information associated with an algorithm which implements some key
    part of a process. In most cases this is quite a high level concept and isn't intended
    to describe the gory detail of how the code implements the algorithm rather the key
    scientific aspects of the algorithm. In particular, it provides a method
    of grouping variables which take part in an algorithm within a process.

    """
    return {
        'type': 'class',
        'base': None,
        'is_abstract': False,
        'properties': [
            ('diagnostic_variables', 'data.variable_collection', '0.N',
                "Diagnostic variables associated with this algorithm."),
            ('heading', 'str', '1.1',
                "Title for this collection of algorithm/property information."),
            ('implementation_overview', 'str', '1.1',
                "Overview of the algorithm implementation."),
            ('prognostic_variables', 'data.variable_collection', '0.N',
                "Prognostic variables associated with this algorithm."),
            ('references', 'shared.citation', '0.N',
                "Relevant references.")
        ]
    }


def conservation_properties():
    """Describes how prognostic variables are conserved.

    """
    return {
        'type': 'class',
        'base': None,
        'is_abstract': False,
        'properties': [
            ('corrected_conserved_prognostic_variables', 'data.variable_collection', '0.1',
                "Set of variables which are conserved by *more* than the numerical scheme alone."),
            ('correction_methodology', 'str', '0.1',
                "Description of method by which correction was achieved."),
            ('flux_correction_was_used', 'bool', '1.1',
                "Flag to indicate if correction involved flux correction.")
        ]
    }


def extent():
    """Key scientific characteristics of the grid use to simulate a specific domain.
    Note that the extent does not itself describe a grid, so, for example, a polar
    stereographic grid may have an extent of northern boundary 90N, southern boundary
    45N, but the fact that it is PS comes from the grid_type.

    """
    return {
        'type': 'class',
        'base': None,
        'is_abstract': False,
        'pstr': ('%s', ('region_known_as',)),
        'properties': [
            ('eastern_boundary', 'float', '0.1',
                "If not global, eastern boundary in degrees of longitude."),
            ('is_global', 'bool', '1.1',
                "True if horizontal coverage is global."),
            ('maximum_vertical_level', 'float', '0.1',
                "Maximum vertical level."),
            ('minimum_vertical_level', 'float', '0.1',
                "Minimum vertical level."),
            ('northern_boundary', 'float', '0.1',
                "If not global, northern boundary in degrees of latitude."),
            ('region_known_as', 'str', '0.N',
                "Identifier or identifiers for the region covered by the extent."),
            ('southern_boundary', 'float', '0.1',
                "If not global, southern boundary in degrees of latitude."),
            ('western_boundary', 'float', '0.1',
                "If not global, western boundary in degrees of longitude."),
            ('z_units', 'str', '1.1',
                "Units of vertical measure.")
        ]
    }


def grid_summary():
    """Key scientific characteristics of the grid use to simulate a specific domain.

    """
    return {
        'type': 'class',
        'base': None,
        'is_abstract': False,
        'properties': [
            ('grid_extent', 'science.extent', '1.1',
                "The extent of the computational domain in horizontal and vertical space."),
            ('grid_layout', 'science.grid_layouts', '1.1',
                "Type of horizontal grid-layout (e.g. Arakawa C-Grid."),
            ('grid_type', 'science.grid_types', '1.1',
                "Description of basic grid (e.g. 'cubed-sphere').")
        ]
    }


def model():
    """A model component: can be executed standalone, and has as scientific
    description available via a link to a science.domain document. (A configured model can
     be understood in terms of a simulation, a model, and a configuration.).

    """
    return {
        'type': 'class',
        'base': 'software.component_base',
        'is_abstract': False,
        'properties': [
            ('category', 'science.model_types', '1.1',
                "Generic type for this model."),
            ('coupled_software_components', 'science.model', '0.N',
                "Software components which are linked together using a coupler to deliver this model."),
            ('coupler', 'software.coupling_framework', '0.1',
                "Overarching coupling framework for model."),
            ('extra_conservation_properties', 'science.conservation_properties', '0.1',
                "Details of any extra methodology needed to conserve variables between coupled components."),
            ('internal_software_components', 'software.software_component', '0.N',
                "Software modules which together provide the functionality for this model."),
            ('link_to_coupled_software_components', 'shared.doc_reference', '0.N',
                "Reference to linked document(s)."),
            ('link_to_scientific_domain', 'shared.doc_reference', '0.N',
                "Reference to linked document(s)."),
            ('meta', 'shared.doc_meta_info', '1.1',
                "Metadata about how the model description was constructed."),
            ('scientific_domain', 'science.scientific_domain', '0.N',
                "The scientific domains which this model simulates.")
        ]
    }


def process():
    """Provides structure for description of a process simulated within a particular
    area (or domain/realm/component) of a model. This will often be subclassed
    within a specific implementation so that constraints can be used to ensure
    that the process details requested are consistent with project requirements
    for information.

    """
    return {
        'type': 'class',
        'base': None,
        'is_abstract': False,
        'properties': [
            ('algorithms', 'science.algorithm', '0.N',
                "Descriptions of algorithms and their properties used in the process."),
            ('description', 'str', '0.1',
                "Short description of the process which is being simulated."),
            ('implementation_overview', 'str', '1.1',
                "General overview description of the implementation of this process."),
            ('keywords', 'str', '1.1',
                "keywords to help re-use and discovery of this information."),
            ('name', 'str', '1.1',
                "Short name for the process of interest."),
            ('properties', 'science.process_detail', '0.N',
                "Sets of properties for this process."),
            ('references', 'shared.reference', '0.N',
                "Any relevant references describing this process and/or it's implementation."),
            ('sub_processes', 'science.sub_process', '0.N',
                "Discrete portion of a process with common process details."),
            ('time_step_in_process', 'float', '0.1',
                "Timestep (in seconds). Only needed if differing from parent component.")
        ]
    }


def process_detail():
    """Provides detail of specific properties of a process, there are two possible specialisations
    expected: (1) A detail_vocabulary is identified, and a cardinality is assigned to that
    for possible responses, or (2) Process_Detail is used to provide a collection for a set of
    properties which are defined in the sub-class. However, those properties must have a type
    which is selected from the classmap (that is, standard 'non-es-doc' types).

    """
    return {
        'type': 'class',
        'base': None,
        'is_abstract': False,
        'properties': [
            ('cardinality_of_selection', 'science.selection_cardinality', '0.1',
                "Required cardinality of selection from vocabulary."),
            ('content', 'str', '0.1',
                "Free text description of process detail (if required)."),
            ('detail_selection', 'str', '0.N',
                "List of choices from the vocabulary of possible detailed options."),
            ('detail_vocabulary', 'str', '0.1',
                "Name of an enumeration vocabulary of possible detail options."),
            ('heading', 'str', '0.1',
                "A heading for this detail description.")
        ]
    }


def resolution():
    """Describes the computational spatial resolution of a component or process. Not intended
        to replace or replicate the output grid description.  When it appears as part of a process
        description, provide only properties that differ from parent domain. Note that where
        different variables have different grids, differences in resolution can be captured by
        repeating the number_of_ properties.

    """
    return {
        'type': 'class',
        'base': None,
        'is_abstract': False,
        'properties': [
            ('equivalent_horizontal_resolution', 'float', '1.1',
                "Resolution in metres of 'typical grid cell' (for gross comparisons of resolution), eg. 50000 (50km)."),
            ('is_adaptive_grid', 'bool', '0.1',
                "Default is False, set true if grid resolution changes during execution."),
            ('name', 'str', '1.1',
                "This is a string usually used by the modelling group to describe their model component  or process resolution,  e.g. N512L180 or T512L70 etc."),
            ('number_of_levels', 'int', '0.N',
                "Number of vertical levels resolved."),
            ('number_of_xy_gridpoints', 'int', '0.N',
                "Total number of horizontal points on computational grids.")
        ]
    }


def scientific_domain():
    """Scientific area of a numerical model - usually a sub-model or component.
    Can also be known as a realm.

    """
    return {
        'type': 'class',
        'base': None,
        'is_abstract': False,
        'properties': [
            ('extra_conservation_properties', 'science.conservation_properties', '0.1',
                "Details of any extra methodology needed to conserve variables between processes."),
            ('grid', 'science.grid_summary', '0.1',
                "Summary description of the grid upon which computations were carried out."),
            ('meta', 'shared.doc_meta_info', '1.1',
                "Metadata describing the construction of this domain description."),
            ('name', 'str', '1.1',
                "Name of the scientific domain (e.g. ocean)."),
            ('overview', 'str', '0.1',
                "Free text overview description of key properties of domain."),
            ('realm', 'str', '0.1',
                "Canonical name for the domain of this scientific area."),
            ('references', 'shared.reference', '0.N',
                "Any relevant references describing the implementation of this domain in a relevant model."),
            ('resolution', 'science.resolution', '1.1',
                "Default resolution of component."),
            ('simulates', 'science.process', '1.N',
                "Processes simulated within the domain."),
            ('time_step', 'float', '1.1',
                "Timestep (in seconds) of overall component."),
            ('tuning_applied', 'science.tuning', '0.1',
                "Describe any tuning used to optimise the parameters in this model/component.")
        ]
    }


def selection_cardinality():
    """Provides the possible cardinalities for selecting from a controlled vocabulary.

    """
    return {
        'type': 'enum',
        'is_open': False,
        'members': [
            ("0.1", "Zero or one selections are permitted"),
            ("0.N", "Zero or many selections are permitted"),
            ("1.1", "One and only one selection is required"),
            ("1.N", "At least one, and possibly many, selections are required")
        ]
    }


def sub_process():
    """Provides structure for description of part of process simulated within a particular
    area (or domain/realm/component) of a model. Typically this will be a part of process
    which shares common properties. It will normally be sub classed within a specific
    implementation so that constraints can be used to ensure that the process details requested are
    consistent with projects requirements for information.

    """
    return {
        'type': 'class',
        'base': None,
        'is_abstract': False,
        'properties': [
            ('description', 'str', '0.1',
                "Short description of the sub-process context."),
            ('implementation_overview', 'str', '0.1',
                "General overview description of the implementation of this part of the process."),
            ('keywords', 'str', '0.1',
                "keywords to help re-use and discovery of this information."),
            ('name', 'str', '1.1',
                "Short name for the collection of sub-process properties."),
            ('properties', 'science.process_detail', '0.N',
                "Sets of properties for this process."),
            ('references', 'shared.reference', '0.N',
                "Any relevant references describing this part of the process and/or it's implementation.")
        ]
    }


def tuning():
    """Method used to optimise equation parameters in model component (aka 'tuning').

    """
    return {
        'type': 'class',
        'base': None,
        'is_abstract': False,
        'properties': [
            ('description', 'str', '1.1',
                "Brief description of tuning methodology. Include information about observational period(s) used."),
            ('global_mean_metrics_used', 'data.variable_collection', '0.1',
                "Set of metrics of the global mean state used in tuning model parameters."),
            ('regional_metrics_used', 'data.variable_collection', '0.1',
                "Which regional metrics of mean state (e.g Monsoons, tropical means etc) have been used in tuning."),
            ('trend_metrics_used', 'data.variable_collection', '0.1',
                "Which observed trend metrics have been used in tuning model parameters.")
        ]
    }