from openerp.osv import osv, fields
import openerp
# For warnings
from openerp.tools.translate import _

class erp_emploi(osv.osv):

    _name = 'erp.emploi'

    _columns = {
        'emploi': fields.binary("Emploi", required = True),
        # TODO : add relationship with classe
    }

    # a method to validate file extensions
    def _check_extension(self, cr, uid, ids, context=None):
        for emploi in self.browse(cr, uid, ids, context=context):
            extension = emploi.emploi.split('.')[-1]
            if extension not in ["pdf", "csv", "docx", "jpeg"]:
                raise openerp.exceptions.Warning(
                    _('The file should be of type pdf, csv, jpg'))
        return True

    # Constraints to validate inputs:
    _constraints = [
        (_check_extension, 'The file should be of type pdf, csv, jpeg', ['emploi']),
    ]

erp_emploi()
