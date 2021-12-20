from openerp.osv import osv, fields
import openerp


class erp_classe(osv.osv):

    _name = 'erp.classe'

    _columns = {
        'classe': fields.char("Classe", required = True, size = 30),
        'code': fields.char("Code", required = True, size = 10),
        'etudiant_ids': fields.one2many('erp.etudiant', 'id_classe', string='Etudiant'),
    }


erp_classe()
