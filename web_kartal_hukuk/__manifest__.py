# -*- coding: utf-8 -*-
{
    'name': "Kartal Hukuk Website",
    'author': "Vismarin Bilişim",
    'website': "http://www.vismarin.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Website',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'web', 'website','mail'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',

        'views/home_page.xml',
        'views/about_page.xml',
        'views/team_page.xml',
        'views/team_page_details.xml',
        'views/deputation_page.xml',
        'views/activities_page_details.xml',
        'views/activities_page.xml',
        'views/links_page.xml',
        'views/contact_page.xml',
        'views/mail_template.xml',
        'views/login_page.xml',
        'views/article_page.xml',
        'views/article_page_detail.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
