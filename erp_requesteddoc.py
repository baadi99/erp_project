from openerp.osv import osv, fields
import openerp

class erp_requesteddoc(osv.osv):

    _name = 'erp.requesteddoc'

    _columns = {
        'name': fields.char("Type", required = True, size = 50),
        # TODO: add one2many relationship with request
        'request_ids': fields.one2many('erp.request', 'type_id', string = 'Document Requests'),
        # TODO: add field 'Template' 
    }


erp_requesteddoc()
