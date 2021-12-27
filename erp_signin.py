from openerp.osv import osv, fields
import openerp

class erp_signin(osv.osv):

    _name = 'erp.signin'

    _columns = {
        'date_signin': fields.date("Date", required = True),
        'student_id': fields.many2one('erp.student', 'Student', ondelete='cascade', required = True),
        'classe_id': fields.many2one('erp.classe', 'Class', ondelete='cascade', required = True),
    }

    _defaults = {
        'date_signin': fields.date("date").today(),    
    }


erp_signin()
