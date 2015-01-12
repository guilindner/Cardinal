# -*- coding: utf-8 -*-

from openerp.osv import osv, fields, expression

class product_product(osv.osv):
    _name = "product.template"
    _inherit = "product.template"

    _columns = {
                'car_aplicacao': fields.char('Aplicação', size=20, help="Produto ou componente onde este item é utilizado"),
    }

product_product()
