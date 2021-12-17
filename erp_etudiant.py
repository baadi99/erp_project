from openerp.osv import osv, fields
import openerp

class erp_etudiant(osv.osv):

    _name ='erp.etudiant'

    _columns = {
        'fname': fields.char("First name", size = 20),
        'lname': fields.char("Last name", size = 20),
        'telephone': fields.char("Telephone", size = 10),
        'email': fields.char("Email", size = 50),
        'gender': fields.char("Gender", size = 10),
        'birth_date': fields.date("Date of birth"),
        'birth_location': fields.char("Birth location", size = 50),
        'cin': fields.char("CIN", size = 10),
        'inscrit': fields.boolean('Inscrit'),
    }

    _defaults = {
        'inscrit': False,
    }



erp_etudiant()
