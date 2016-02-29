# -*- coding: utf-8 -*-

"""
.. module:: shared_classes.py
   :synopsis: Set of CIM v2 ontology type definitions.

"""


def cimtext():
    """Provides a text class which supports plaintext, html, and
    friends (or will do).

    """
    return {
        'type': 'class',
        'base': None,
        'is_abstract': False,
        'pstr': ('%s', ('content',)),
        'properties': [
            ('content', 'str', '1.1',
                "Raw content (including markup)."),
            ('content_type', 'shared.text_code', '1.1',
                "Type of content.")
        ]
    }


def doc_meta_info():
    """Encapsulates document meta information used by es-doc machinery. Will not normally be
    populated by humans. May duplicate information held in 'visible' metadata.

    """
    return {
        'type': 'class',
        'base': None,
        'is_abstract': False,
        'properties': [
            ('author', 'shared.party', '0.1',
                "Author of the metadata in the parent document."),
            ('create_date', 'datetime', '1.1',
                "Date upon which the instance was created."),
            ('drs_keys', 'str', '0.N',
                "DRS related keys to support correlation of documents with datasets."),
            ('drs_path', 'str', '0.1',
                "DRS related path to support documents with datasets."),
            ('external_ids', 'str', '0.N',
                "Set of identifiers used to reference the document by external parties."),
            ('id', 'str', '1.1',
                "Universal document identifier (normally a UUID)."),
            ('institute', 'str', '0.1',
                "Name of institute with which instance is associated with."),
            ('language', 'str', '1.1',
                "Language with which instance is associated with."),
            ('project', 'str', '1.1',
                "Name of project with which instance is associated with."),
            ('sort_key', 'str', '0.1',
                "Document sort key."),
            ('source', 'str', '1.1',
                "Name of application that created the instance."),
            ('source_key', 'str', '0.1',
                "Key of application that created the instance."),
            ('type', 'str', '1.1',
                "Document ontology type."),
            ('type_display_name', 'str', '0.1',
                "Document type display name."),
            ('type_sort_key', 'str', '0.1',
                "Document type sort key."),
            ('update_date', 'datetime', '1.1',
                "Date upon which the instance was last updated."),
            ('version', 'int', '1.1',
                "Document version identifier.")
        ]
    }


def doc_reference():
    """Specialisation of online resource for link between CIM documents, whether the
    remote document exists when complete, or not.

    """
    return {
        'type': 'class',
        'base': 'shared.online_resource',
        'is_abstract': False,
        'properties': [
            ('constraint_vocabulary', 'str', '0.1',
                "A constraint vocabulary for the relationship."),
            ('context', 'str', '0.1',
                "Information about remote record in context of reference."),
            ('id', 'str', '0.1',
                "Identifier of remote resource, if known."),
            ('relationship', 'str', '0.1',
                "Predicate - relationship of the object target as seen from the subject resource."),
            ('type', 'str', '1.1',
                "The type of the remote record."),
            ('version', 'int', '0.1',
                "The version of the remote record.")
        ]
    }


def document_types():
    """The complete set of CIM document types, that is, all classes which carry the
    document metadata attributes.

    """
    return {
        'type': 'enum',
        'is_open': False,
        'members': [
            ("Conformance", None),
            ("Dataset", None),
            ("DomainProperties", None),
            ("Downscaling", None),
            ("Ensemble", None),
            ("EnsembleRequirement", None),
            ("ExternalDocument", None),
            ("ForcingConstraint", None),
            ("Grid", None),
            ("Machine", None),
            ("Model", None),
            ("MultiEnsemble", None),
            ("MultiTimeEnsemble", None),
            ("NumericalExperiment", None),
            ("NumericalRequirement", None),
            ("OutputTemporalRequirement", None),
            ("Party", None),
            ("Performance", None),
            ("Project", None),
            ("ScientificDomain", None),
            ("Simulation", None),
            ("SimulationPlan", None),
            ("TemporalConstraint", None),
            ("UberEnsemble", None)
        ]
    }





def key_float():
    """Holds a key and a float value.

    """
    return {
        'type': 'class',
        'base': None,
        'is_abstract': False,
        'pstr': ('%s: %s', ('key', 'value')),
        'properties': [
            ('key', 'str', '1.1',
                "User defined key."),
            ('value', 'float', '1.1',
                "Value associated with a key (real number).")
        ]
    }


def nil_reason():
    """Provides an enumeration of possible reasons why a property has not been defined
    Based on GML nilReason as discussed here: https://www.seegrid.csiro.au/wiki/AppSchemas/NilValues.

    """
    return {
        'type': 'enum',
        'is_open': False,
        'members': [
            ("nil:inapplicable", "There is no value"),
            ("nil:missing", "The correct value is not available. Furthermore, a correct value may not exist"),
            ("nil:template", "The value will be available later"),
            ("nil:unknown", "The correct value is not known at this time. However, a correct value probably exists"),
            ("nil:withheld", "The value is not divulged")
        ]
    }


def number_array():
    """Provides a class for entering an array of numbers.

    """
    return {
        'type': 'class',
        'base': None,
        'is_abstract': False,
        'pstr': ('%s', ('values',)),
        'properties': [
            ('values', 'str', '1.1',
                "A space separated list of numbers.")
        ]
    }


def online_resource():
    """A minimal approximation of ISO19115 CI_ONLINERESOURCE, provides a link and details
    of how to use that link.

    """
    return {
        'type': 'class',
        'base': None,
        'is_abstract': False,
        'properties': [
            ('description', 'str', '0.1',
                "Detail of how to access the resource."),
            ('linkage', 'str', '1.1',
                "A URL."),
            ('name', 'str', '1.1',
                "Name of online resource."),
            ('protocol', 'str', '0.1',
                "Protocol to use at the linkage.")
        ]
    }


def party():
    """Implements minimal material for an ISO19115-1 (2014) compliant party.
    For our purposes this is a much better animal than the previous responsibleParty 
    which munged roles together with people. Note we have collapsed CI_Contact,
    CI_Individual and CI_Organisation as well as the abstract CI_Party.

    """
    return {
        'type': 'class',
        'base': None,
        'is_abstract': False,
        'properties': [
            ('address', 'str', '0.1',
                "Institutional address."),
            ('email', 'str', '0.1',
                "Email address."),
            ('meta', 'shared.doc_meta_info', '1.1',
                "Provides a unique identifier for the party."),
            ('name', 'str', '0.1',
                "Name of person or organisation."),
            ('orcid_id', 'str', '0.1',
                "Orcid ID if available."),
            ('organisation', 'bool', '0.1',
                "True if an organisation not a person."),
            ('url', 'shared.online_resource', '0.1',
                "URL of person or institution.")
        ]
    }


def pid():
    """A permanent identifier (with a resolution service).

    """
    return {
        'type': 'class',
        'base': None,
        'is_abstract': False,
        'properties': [
            ('id', 'str', '1.1',
                "The identifier."),
            ('resolution_service', 'shared.online_resource', '1.1',
                "The resolution service.")
        ]
    }


def quality_review():
    """Assertations as to the completeness and quality of a document.

    """
    return {
        'type': 'class',
        'base': None,
        'is_abstract': False,
        'properties': [
            ('date', 'str', '1.1',
                "Date upon which review was made."),
            ('metadata_reviewer', 'linked_to(shared.party)', '1.1',
                "Party who made the metadata quality assessment."),
            ('quality_description', 'str', '1.1',
                "Assessment of quality of this document."),
            ('quality_status', 'shared.quality_status', '0.1',
                "Status from a controlled vocabulary.")
        ]
    }


def quality_status():
    """None

    """
    return {
        'type': 'enum',
        'is_open': False,
        'members': [
            ("incomplete", "Currently being worked on"),
            ("finalised", "Author has completed document, prior to review"),
            ("under_review", "Document is being reviewed"),
            ("reviewed", "Document has been formally reviewed and assessed as complete and accurate")
        ]
    }


def external_document():
    """A real world document, could be a book, a journal article, a manual, a web page ... it might or might
    not be online, although preferably it would be. We expect a typical citation to be built up
    as in the following 'authorship, date: title, publication_detail (doi if present)'.

    """
    return {
        'type': 'class',
        'base': None,
        'is_abstract': False,
        'pstr': ('%s', ('name',)),
        'properties': [
            ('authorship', 'str', '0.1',
                "List of authors expressed using an appropriate syntax."),
            ('date', 'str', '0.1',
                "Date of publication, or of access in the case of a URL."),
            ('doi', 'str', '0.1',
                "Digital Object Identifier, if it exists."),
            ('meta', 'shared.doc_meta_info', '1.1',
                "Metadata about the creation of this document description."),
            ('name', 'str', '1.1',
                "A name for the citation: short hand description, e.g. Meehl et al (2014)."),
            ('online_at', 'shared.online_resource', '0.1',
                "Location of electronic version."),
            ('publication_detail', 'str', '0.1',
                "Journal/publisher, page and volume information as appropriate."),
            ('title', 'str', '1.1',
                "Title or name of the document.")
        ]
    }


def reference():
    """An external document which can have a context associated with it.

    """
    return {
        'type': 'class',
        'base': None,
        'is_abstract': False,
        'properties': [
            ('context', 'str', '0.1',
                "Brief text description of why this resource is being cited."),
            ('document', 'shared.external_document', '1.1',
                "Reference Target.")
        ]
    }


def responsibility():
    """Implements the ISO19115-1 (2014) CI_Responsibility (which replaces
    responsibleParty). Combines a person and their role in doing something.

    """
    return {
        'type': 'class',
        'base': None,
        'is_abstract': False,
        'pstr': ('%s:%s', ('role', 'party')),
        'properties': [
            ('party', 'linked_to(shared.party)', '1.N',
                "Parties delivering responsibility."),
            ('role', 'shared.role_code', '1.1',
                "Role that the party plays or played."),
            ('when', 'shared.time_period', '0.1',
                "Period when role was active, if no longer.")
        ]
    }


def role_code():
    """Responsibility role codes: roles that a party may play in delivering a responsibility.

    """
    return {
        'type': 'enum',
        'is_open': False,
        'members': [
            ("Principal Investigator", "Key party responsible for the existence of the resource"),
            ("originator", "Original source for the resource if obtained from elsewhere"),
            ("author", "Party who created (or co-created) resource"),
            ("collaborator", "Contributor to the production of the resource"),
            ("publisher", "Party who published the resource"),
            ("owner", "Party with legal ownership of the resource"),
            ("processor", "Party who has taken part in the workflow that resulted in this resource"),
            ("distributor", "Party who distributes the resource"),
            ("sponsor", "Party who has invested in the production of the resource"),
            ("user", "Party who uses the resource"),
            ("point of contact", "Party who can be contacted for acquiring knowledge about or acquisition of the resource"),
            ("resource provider", "Party that supplies the resource"),
            ("custodian", "Party that accepts accountability and responsibility for the source resource"),
            ("metadata_reviewer", "Party who carried out an independent review of (this) documentation"),
            ("metadata_author", "Party who created (this) documentation")
        ]
    }


def text_code():
    """Types of text understood by the CIM notebook. Currently only
    plaintext, but we expect safe HTML to be supported as soon as practicable.

    """
    return {
        'type': 'enum',
        'is_open': False,
        'members': [
            ("plaintext", "Normal plain text")
        ]
    }
