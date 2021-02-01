# -*- coding: utf-8 -*-
{
    'name': "Kartal Hukuk Bürosu",
    'author': "Vismarin Bilişim",
    'website': "http://www.vismarin.com",

    'category': 'Website',
    'version': '0.1',
    'depends': ['base'],
    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/personnel_views.xml',
        'views/activities_views.xml',
        'views/contact_views.xml',
        'views/article_views.xml',


    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application': True,
}
