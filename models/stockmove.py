from openerp import models, fields, api, exceptions, _


class Production(models.Model):
    _inherit = 'stock.move'

    bad_rate = fields.Float(_compute="_compute_bad_rate")

    @api.depends("picking_id.pack_operation_ids")
    @api.one
    def _compute_bad_rate(self):
        ops = self.picking_id.pack_operation_ids
        loc_id = self.env["stock.location"].ref("mrp_miaoyin.stock_location_bad_product").id
        #if ops:
        bad_count = sum((op.product_qty for op in ops if op.location_dest_id.id == loc_id))
        self.bad_rate = 0.5 # float(bad_count) / self.product_qty
