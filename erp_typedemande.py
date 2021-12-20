from openerp.osv import osv, fields
import openerp


class erp_typedemande(osv.osv):

    _name = 'erp.typedemande'

    _columns = {
        'type_demande': fields.char("Type", required = True, size = 20)
        # TODO: add one2many relationship with demande
        # TODO: add field 'Template' 
    }


erp_typedemande()
