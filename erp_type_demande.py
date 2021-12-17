from openerp.osv import osv, fields
import openerp


class erp_type_demande(osv.osv):

    _name = 'erp.type_demande'

    _columns = {
        'type': fields.char("Type", size=20),
    }


erp_type_demande()
