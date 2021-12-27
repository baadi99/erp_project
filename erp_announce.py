from openerp.osv import osv, fields
import openerp

import logging
_logger = logging.getLogger(__name__)

class erp_announce(osv.osv):

    _name = 'erp.announce'

    _columns = {
        'file_name': fields.char("file name", required = True), # a helper field to store the name of the uploaded file
        'announce_file': fields.binary("Announce", required = True),
        'type_announce': fields.selection((("1", "Affichage"), ("2","Deliberation")), string = "Type", required = True),
        # 'classe_id': fields.many2one('erp.classe', 'Class', ondelete='cascade'),
    }

    _defaults = {
        'type_announce': "1",
    }


    # a method to validate file extensions
    def _check_extension(self, cr, uid, ids, context=None):
        for announce in self.browse(cr, uid, ids, context=context):
            extension = announce.file_name.split('.')[-1].lower()
            if extension and extension not in ["pdf", "csv", "docx", "jpeg", "jpg"]:
                raise openerp.exceptions.Warning('The file should be of type pdf, csv, jpeg/jpg')
        return True

    # Constraints to validate inputs: 
    _constraints = [
        (_check_extension, 'The file should be of type pdf, csv, jpeg/jpg', ['file_name']),
    ]

erp_announce()
