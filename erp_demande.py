from openerp.osv import osv, fields
import openerp

class erp_demande(osv.osv):

    _name = 'erp.demande'

    _columns = {
        'date_demande': fields.date("Date"),
        'status': fields.selection((('1', 'Pending'), ('2', 'Processed')), string = 'Status', required = True),
        # TODO: add many2one relationship with typeDemande
    }

    _defaults = {
        'date_demande': fields.date("Date").today()
    }

    # Mark a request as done
    def demande_processed(self, cr, uid, ids, context=None):
        return self.write(cr, uid, ids, {'status': '2'}, context=context)

erp_demande()
