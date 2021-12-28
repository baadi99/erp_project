from openerp.osv import osv, fields
import openerp


class erp_announcement(osv.osv):

    _name = 'erp.announcement'

    _columns = {
        'file_name': fields.char("file name", required = True), # a helper field to store the name of the uploaded file
        'announcement_file': fields.binary("Announcement", required = True),
        'type_announcement': fields.selection((("1", "Affichage"), ("2","Deliberation")), string = "Type", required = True),
        # 'classe_id': fields.many2one('erp.classe', 'Class', ondelete='cascade'),
    }

    _defaults = {
        'type_announcement': "1",
    }


    # a method to validate file extensions
    def _check_extension(self, cr, uid, ids, context=None):
        for announcement in self.browse(cr, uid, ids, context=context):
            extension = announcement.file_name.split('.')[-1].lower()
            if extension and extension not in ["pdf", "csv", "docx", "jpeg", "jpg"]:
                raise openerp.exceptions.Warning('The file should be of type pdf, csv, jpeg/jpg')
        return True

    # Constraints to validate inputs: 
    _constraints = [
        (_check_extension, 'The file should be of type pdf, csv, jpeg/jpg', ['file_name']),
    ]

erp_announcement()
