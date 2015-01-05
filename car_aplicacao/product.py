# -*- coding: utf-8 -*-

class product_product(osv.osv):
    _inherit = "product.product"

    _columns = {
                'car_aplicacao': fields.char('Aplicação', size=20),
                                    help="Produto ou componente onde a peça pode ser utilizada."),
    }

product_product()
