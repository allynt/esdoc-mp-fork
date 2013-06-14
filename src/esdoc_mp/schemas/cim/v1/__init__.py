"""
.. module:: esdoc_mp.schemas.cim.v1.__init__.py
   :copyright: Copyright "Feb 7, 2013", Earth System Documentation
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Sub-package initializer.

.. moduleauthor:: Mark Conway-Greenslade (formerly Morgan) <momipsl@ipsl.jussieu.fr>


"""

# Module imports.
from esdoc_mp.schemas.cim.v1.activity import package as activity_package
from esdoc_mp.schemas.cim.v1.data import package as data_package
from esdoc_mp.schemas.cim.v1.grids import package as grids_package
from esdoc_mp.schemas.cim.v1.quality import package as quality_package
from esdoc_mp.schemas.cim.v1.shared import package as shared_package
from esdoc_mp.schemas.cim.v1.software import package as software_package


# Schema :: CIM v1.
schema = {
    'name' : 'cim',
    'version' : '1',
    'is_latest' : True,
    'doc' : 'Metafor CIM ontology schema - version 1.X',
    'packages' : [
        activity_package,
        data_package,
        grids_package,
        quality_package,
        shared_package,
        software_package
    ]
}
