from openerp.osv import osv, fields
import openerp

class erp_demande(osv.osv):

    _name = 'erp.demande'

    _columns = {
        'date_demande': fields.date("Date"),
        'realise': fields.selection([('1', 'En cours'), ('2', 'Realise')], string = 'Etat'),
    }

    _defaults = {
        
    }


erp_demande()
