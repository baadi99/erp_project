from openerp.osv import osv, fields
import openerp


class erp_affichage(osv.osv):

    _name = 'erp.affichage'

    _columns = {
        'affichage': fields.binary("affichage"),
    }

erp_affichage()
