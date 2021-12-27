from openerp.osv import osv, fields
import openerp


class erp_typedemande(osv.osv):

    _name = 'erp.typedemande'

    _columns = {
        'name': fields.char("Type", required = True, size = 20),
        # TODO: add one2many relationship with demande
        'demande_ids': fields.one2many('erp.demande', 'type_id', string = 'Demandes'),
        # TODO: add field 'Template' 
    }


erp_typedemande()
