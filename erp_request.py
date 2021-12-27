from openerp.osv import osv, fields
import openerp


import logging
_logger = logging.getLogger(__name__)

class erp_request(osv.osv):

    _name = 'erp.request'

    # Needed for emails
    _inherit = ['mail.thread']

    _columns = {
        'request_date': fields.date("Date"),
        'email': fields.char('email', readonly=True), # needed for mailing feature
        'status': fields.selection((("1", "Pending"), ("2", "Processed")), string = "Status", required = True),
        'type_id': fields.many2one('erp.requesteddoc', 'Requested Document', ondelete='cascade', required = True),
        'student_id': fields.many2one('erp.student', 'Student', ondelete='cascade', required=True),
        'email_notif_id' : fields.many2one('email.template', 'Notification email template'),
    }

    _defaults = {
        'request_date': fields.date("Date").today(),
        'status': "1",
    }

    # def send_notif_email(self, cr, uid, ids, context=None):
    #     """
    #     Send email to user when the event is confirmed
    #     """
    #     for request in self.browse(cr, uid, ids, context=context):
    #         template_id = request.email_notif_id.id
    #         if template_id:
    #             self.pool.get('email.template').send_mail(
    #                 cr, uid, template_id, request.id, context=context)
    #     return True

    # Mark a request as done
    def request_processed(self, cr, uid, ids, context=None):
        return self.write(cr, uid, ids, {'status': "2"}, context=context)

erp_request()
