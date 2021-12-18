from openerp.osv import osv, fields
import openerp


class erp_typedemande(osv.osv):

    _name = 'erp.typedemande'

    _columns = {
        'type_demande': fields.char("Type", required = True, size = 20)
    }


erp_typedemande()
