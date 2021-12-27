from openerp.osv import osv, fields
import openerp

class erp_inscription(osv.osv):

    _name = 'erp.inscription'

    _columns = {
        'date_inscription': fields.date("Date", required = True),
        'etudiant_id': fields.many2one('erp.etudiant', 'Etudiant', ondelete='set null', required = True),
        'classe_id': fields.many2one('erp.classe', 'Classe', ondelete='set null', required = True),
    }

    _defaults = {
        'date_inscription': fields.date("date").today(),    
    }


erp_inscription()
