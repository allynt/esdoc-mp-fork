"""
The cim v1.5 ontology - shared package.
"""

# Module imports.
from esdoc_mp.schemas.cim.v1_5.shared.classes import classes
from esdoc_mp.schemas.cim.v1_5.shared.classes_cim import classes as cim_classes
from esdoc_mp.schemas.cim.v1_5.shared.classes_time import classes as time_classes
from esdoc_mp.schemas.cim.v1_5.shared.enums import enums


# Module exports.
__all__ = ["package"]


# Module provenance info.
__author__="markmorgan"
__copyright__ = "Copyright 2010, Insitut Pierre Simon Laplace - Prodiguer"
__date__ ="$Jun 28, 2010 2:52:22 PM$"
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Sebastien Denvil"
__email__ = "sdipsl@ipsl.jussieu.fr"
__status__ = "Production"

# CIM v1.5 - shared package.
package = {
    'name' : 'shared',
    'doc' : 'TODO get package documentation',
    'classes' : classes + cim_classes + time_classes,
    'enums' : enums,
}
