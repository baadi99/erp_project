from openerp.osv import osv, fields
import openerp

class erp_emploi(osv.osv):

    _name = 'erp.emploi'

    _columns = {
        'emploi': fields.binary("Emploi", filters = "*.pdf, *.jpeg" , required = True),
    }

erp_emploi()
