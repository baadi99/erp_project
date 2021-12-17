from openerp.osv import osv, fields
import openerp

class erp_emploi(osv.osv):

    _name = 'erp.emploi'

    _columns = {
        'emploi': fields.binary("Date"),
    }

erp_emploi()
