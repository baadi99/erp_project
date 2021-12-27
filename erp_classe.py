from openerp.osv import osv, fields
import openerp


class erp_classe(osv.osv):

    _name = 'erp.classe'

    # A method to get the name of the current classe formated as classe, code
    def _get_class_name(self, cr, uid, ids, field_name, arg, context=None):
        class_name = {}
        for classe in self.browse(cr, uid, ids, context):
            if not classe.classe == "":
                class_name[classe.id] = classe.classe
            if not classe.code == "":
                class_name[classe.id] += ", " + classe.code
        return class_name

    _columns = {
        # name is a helper field that will be used in relationships
        # instead of displayed as erp.classe,id the relationship
        # will display in the "classe, code" format
        'name': fields.function(_get_class_name, type='char', store = True),
        'classe': fields.char("Classe", required = True, size = 30),
        'code': fields.char("Code", required = True, size = 10),
        'etudiant_ids': fields.one2many('erp.etudiant', 'classe_id', string='Etudiant'),
        'inscription_ids': fields.one2many('erp.inscription', 'classe_id', string='Inscriptions'),
        'emploi_ids': fields.one2many('erp.emploi', 'classe_id', string='Emplois'),
        'affichage_ids': fields.one2many('erp.affichage', 'classe_id', string='Affichages'),
    }


erp_classe()
