from openerp.osv import osv, fields
import openerp
# For warnings
from openerp.tools.translate import _

import logging
_logger = logging.getLogger(__name__)

class erp_affichage(osv.osv):

    _name = 'erp.affichage'

    _columns = {
        'affichage_file': fields.binary("Affichage", required = True),
        'file_name': fields.char("file name"), # a helper field to store the name of the uploaded file
        'type_affichage': fields.selection((("1", "Affichage d'un module"), ("2","Deliberation")), string = "Type d'affichage", required = True),
        # TODO: add many2one relationship with classe
    }


    # # a method to validate file extensions
    # def _check_extension(self, cr, uid, ids, context=None):
    #     for affichage in self.browse(cr, uid, ids, context=context):
    #         extension = affichage.file_name
    #         _logger.info("---------------------------------")
    #         _logger.info("extension: %s", extension)
    #         _logger.info(affichage.file_name)
    #         if extension and extension not in ["pdf", "csv", "docx", "jpeg", "jpg"]:
    #             raise openerp.exceptions.Warning(_('The file should be of type pdf, csv, jpg'))
    #     return True

    # # Constraints to validate inputs: 
    # _constraints = [
    #     (_check_extension, 'The file should be of type pdf, csv, jpeg/jpg', ['file_name']),
    # ]

erp_affichage()
