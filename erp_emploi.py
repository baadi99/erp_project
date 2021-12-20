from openerp.osv import osv, fields
import openerp
# For warnings
from openerp.tools.translate import _

class erp_emploi(osv.osv):

    _name = 'erp.emploi'

    _columns = {
        'file_name': fields.char("File name", required = True),
        'emploi': fields.binary("Emploi", required = True),
        # TODO : add relationship with classe
    }

    # a method to validate file extensions
    def _check_extension(self, cr, uid, ids, context=None):
        for emploi in self.browse(cr, uid, ids, context=context):
            extension = emploi.file_name.split('.')[-1].lower()
            if extension and extension not in ["pdf", "csv", "docx", "jpeg", "jpg"]:
                raise openerp.exceptions.Warning(
                    _('The file should be of type pdf, csv, jpeg/jpg'))
        return True

    # Constraints to validate inputs:
    _constraints = [
        (_check_extension, 'The file should be of type pdf, csv, jpeg/jpg', ['file_name']),
    ]

erp_emploi()
