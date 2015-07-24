from openerp import models, fields, api, exceptions, _


class StockMove(models.Model):
    _inherit = 'stock.move'

    bad_rate = fields.Float(digits=(4, 2), compute="_compute_bad_rate")

    @api.depends("picking_id.pack_operation_ids")
    @api.one
    def _compute_bad_rate(self):
        ops = self.picking_id.pack_operation_ids
        loc_id = self.env.ref("mrp_miaoyin.stock_location_bad_product").id
        if ops and self.state == "done":
            bad_count = sum((op.qty_done for op in ops if op.location_dest_id.id == loc_id and
                             op.product_id.id == self.product_id.id))
            self.bad_rate = float(bad_count) / self.product_uom_qty



