# -*- coding: utf-8 -*-
{
    'name': "car_aplicacao",

    'summary': """
        Adiciona o campo Aplicacao na aba principal dos produtos
        blablabla""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Cardinal",
    'website': "http://www.cardinal.com.br",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Product',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','product'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
       # 'templates.xml',
    ],
}
