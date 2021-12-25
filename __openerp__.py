{
    'name':'Gestion Scolarite',
    'version':'1.0',
    'author':'Mohcine BAADI, Hamza SAKHRI',
    'category':'Gestion',
    'sequence':1,
    'description':"un module qui permet la gestion de scolarite",
    'images':[''],
    'depends': ['base', 'email_template'],
    'data': [
        'erp_etudiant_view.xml', 
        'erp_affichage_view.xml', 
        'erp_demande_view.xml',
        'erp_typedemande_view.xml',
        'erp_emploi_view.xml',
        'erp_inscription_view.xml',
        'erp_classe_view.xml',
        'email_template.xml',
        ],
    'website':'scolarite@gmail.com',
    'update_xml':[],
    'js':[],
    'qweb':[],
    'css':['static/src/css/scolarite.css'],
    'demo':[],
    'test':[],
    'installable':True,
    'auto_install':False
}