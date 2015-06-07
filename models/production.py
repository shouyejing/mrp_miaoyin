from openerp import models, fields, api, exceptions, _


class Production(models.Model):
    _inherit = 'mrp.production'

    location_dest_id = fields.Many2one(default=lambda self: self.env.ref('mrp_miaoyin.stock_location_after_production'),
                                       readonly=True)
    location_src_id = fields.Many2one(readonly=True)

