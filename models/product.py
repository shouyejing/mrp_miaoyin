from openerp import models, fields, api, exceptions, _


class Product(models.Model):
    _inherit = 'product.product'

    category_id = fields.Many2one(related='product_tmpl_id.categ_id', readonly=True)
