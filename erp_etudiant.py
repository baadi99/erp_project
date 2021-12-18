from openerp.osv import osv, fields
import openerp

class erp_etudiant(osv.osv):

    _name ='erp.etudiant'

    _columns = {
        'fname': fields.char("First name", required = True, size = 20),
        'lname': fields.char("Last name", required = True, size=20),
        'telephone': fields.char("Telephone", required = True, size = 10),
        'email': fields.char("Email", required = True, size = 50),
        'gender': fields.selection((('male', 'male'), ('female', 'female')), string = "Gender", required = True),
        'birth_date': fields.date("Date of birth", required = True),
        'birth_location': fields.char("Birth location", required = True, size = 50),
        'cin': fields.char("CIN", required = True, size = 10),
        'inscrit': fields.boolean('Inscrit'),
    }

    _defaults = {
        'inscrit': False,
    }



erp_etudiant()
