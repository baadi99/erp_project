from openerp.osv import osv, fields
import openerp

class erp_registration(osv.osv):

    _name = 'erp.registration'

    _columns = {
        'date_registration': fields.date("Date", required = True),
        'student_id': fields.many2one('erp.student', 'Student', ondelete='cascade', required = True),
        'classe_id': fields.many2one('erp.classe', 'Class', ondelete='cascade', required = True),
    }

    _defaults = {
        'date_registration': fields.date("date").today(),    
    }

    # A method to assign a student to a class and mark them as registred when
    # a new registration is created
    def create(self, cr, uid, values, context = None):
        student = values['student_id']
        self.pool.get('erp.student').write(cr, uid, [student], {'classe_id': values['classe_id'], 'inscrit': True}, context=context)
        return super(erp_registration, self).create(cr, uid, values, context=context)


erp_registration()
