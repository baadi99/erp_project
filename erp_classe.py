from openerp.osv import osv, fields
import openerp


class erp_classe(osv.osv):

    _name = 'erp.classe'

    _columns = {
        'classe': fields.char("Classe", required = True, size = 30),
        'code': fields.char("Code", required = True, size = 10),
    }


erp_classe()
