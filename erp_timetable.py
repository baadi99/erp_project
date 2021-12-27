from openerp.osv import osv, fields
import openerp

class erp_timetable(osv.osv):

    _name = 'erp.timetable'

    _columns = {
        'file_name': fields.char("File name", required = True),
        'timetable': fields.binary("Timetable", required = True),
        'semester': fields.selection((('1', 'S1'), ('2', 'S2')), string = "Semester", required = True),
        # TODO : add relationship with classe
        'classe_id': fields.many2one('erp.classe', 'Class', ondelete='cascade', required=True),
    }

    # a method to validate file extensions
    def _check_extension(self, cr, uid, ids, context=None):
        for timetable in self.browse(cr, uid, ids, context=context):
            extension = timetable.file_name.split('.')[-1].lower()
            if extension and extension not in ["pdf", "csv", "docx", "jpeg", "jpg"]:
                raise openerp.exceptions.Warning('The file should be of type pdf, csv, jpeg/jpg')
        return True

    # Constraints to validate inputs:
    _constraints = [
        (_check_extension, 'The file should be of type pdf, csv, jpeg/jpg', ['file_name']),
    ]

erp_timetable()
