# -*- coding: utf-8 -*-
{
    'name': "Hide Menus for Users",
    'version': "1.0",
    'licence': "LGPL-3",
    'author': "Cybrosys",
    'website': "http://www.cybrosys.com",
    'sequence': 1,
    'application': True,
    'depends': ['base'],
    'auto_install': True,
    'data': [
        'security/ir.model.access.csv',
        'views/hide_menu_views.xml',
        'views/res.users_views.xml',
        'views/menu_views.xml',
    ]
}
