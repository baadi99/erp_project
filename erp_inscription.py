from openerp.osv import osv, fields
import openerp

class erp_inscription(osv.osv):

    _name = 'erp.inscription'

    _columns = {
        'date_inscription': fields.date("Date"),
    }

    _defaults = {
        'date_inscription': fields.date("date").today(),    
    }


erp_inscription()
