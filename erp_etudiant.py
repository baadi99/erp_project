from openerp.osv import osv, fields
import openerp
# For regular expression
import re as regex
# For warnings
from openerp.tools.translate import _

import logging
_logger = logging.getLogger(__name__)

class erp_etudiant(osv.osv):

    def _get_classes(self, cr, uid, context=None):
        obj = self.pool.get('erp.classe')
        ids = obj.search(cr, uid, [])
        res = obj.read(cr, uid, ids, ['classe', 'id'], context)
        res = [(r['id'], r['classe']) for r in res]
        return res
        
    _name ='erp.etudiant'

    _columns = {
        'cne': fields.char("CNE", required = True, size = 20),
        'fname': fields.char("First name", required=True, size=20),
        'lname': fields.char("Last name", required = True, size=20),
        'telephone': fields.char("Telephone", required = True, size = 20),
        'email': fields.char("Email", required = True, size = 50),
        'file_name': fields.char("File name", required = True), # a helper field to store the name of the uploaded image
        'photo': fields.binary("Photo", required = True),
        'gender': fields.selection((('male', 'male'), ('female', 'female')), string = "Gender", required = True),
        'birth_date': fields.date("Date of birth", required = True),
        'birth_location': fields.char("Birth location", required = True, size = 50),
        'cin': fields.char("CIN", required = True, size = 10),
        'inscrit': fields.boolean('Inscrit'),
        # should be changed to set to null
        'id_classe': fields.many2one('erp.classe', 'Classe', ondelete='set null', readonly=True),
        'demande_ids': fields.one2many('erp.demande', 'id_etudiant', string='Demandes', selection = _get_classes),
    }

    # Default values
    _defaults = {
        'inscrit': False,
    }


   
    # Mark a student as signed in for the current year
    def mark_inscrit(self, cr, uid, ids, context = None):
        return self.write(cr, uid, ids, {'inscrit': True}, context = context)


    # Validation methods:
    def _is_email_valid(self, cr, uid, ids, context = None):
        for etudiant in self.browse(cr, uid, ids, context = context):
            if regex.match("^[a-zA-Z0-9._]+@[a-z\.]+\.[a-z]{2,3}$", etudiant.email) == None:
                raise openerp.exceptions.Warning(_('Email address is not valid'))
        return True

    def _is_email_unique(self, cr, uid, ids, context = None):
        for etudiant in self.browse(cr, uid, ids, context=context):
            if etudiant.email and self.search(cr, uid, [('email', '=', etudiant.email)], context=context, count = True) != 1: # 1 instead of 0 because search method counts the record we are validating
                raise openerp.exceptions.Warning(_('Email address already exists!'))                                          # and not only saved records
        return True

    # a method to validate photo extension
    def _check_extension(self, cr, uid, ids, context = None):
        for etudiant in self.browse(cr, uid, ids, context = context):
            extension = etudiant.file_name.split('.')[-1].lower()
            if extension and extension not in ["png", "jpeg", "jpg"]:
                raise openerp.exceptions.Warning(
                    _('The photo you\'ve selected is invalid!\n Please select a jpeg or png image'))
        return True

    # Constraints to validate inputs
    _constraints = [
        (_is_email_valid, 'Please enter a valid email!', ['email']),
        (_is_email_unique, 'This email already exists!', ['email']),
        (_check_extension, 'The photo you selected is invalid! \nPlease select a valid image(i.e. *.png, *.jpeg/jpg)', ['file_name']),
    ]


erp_etudiant()

