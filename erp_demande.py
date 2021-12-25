from openerp.osv import osv, fields
import openerp


import logging
_logger = logging.getLogger(__name__)

class erp_demande(osv.osv):

    _name = 'erp.demande'

    _inherit = ['mail.thread']

    _columns = {
        'date_demande': fields.date("Date"),
        'email': fields.char('email', readonly=True),
        'status': fields.selection((("1", "Pending"), ("2", "Processed")), string = "Status", required = True),
        # TODO: add many2one relationship with typeDemande 
        'id_etudiant': fields.many2one('erp.etudiant', 'Etudiant', ondelete='set null'),
        'email_notif_id' : fields.many2one('email.template', 'Notification email template', help="This template will be used when a request is marked as processed"),
    }

    _defaults = {
        'date_demande': fields.date("Date").today(),
        'status': "1",
    }

    def send_notif_email(self, cr, uid, ids, context=None):
        """
        Send email to user when the event is confirmed
        """
        for demande in self.browse(cr, uid, ids, context=context):
            template_id = demande.email_notif_id.id
            if template_id:
                self.pool.get('email.template').send_mail(
                    cr, uid, template_id, demande.id, context=context)
        return True

    # Mark a request as done
    def demande_processed(self, cr, uid, ids, context=None):
        return self.write(cr, uid, ids, {'status': "2"}, context=context)

erp_demande()
