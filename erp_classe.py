from openerp.osv import osv, fields
import openerp


class erp_classe(osv.osv):

    _name = 'erp.classe'

    _columns = {
        'classe': fields.char("Classe", size = 30),
        'code': fields.char("Code", size = 10),
    }


erp_classe()
