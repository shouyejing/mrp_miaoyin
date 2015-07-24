from openerp import models, fields, api, exceptions, _


class StockMove(models.Model):
    _inherit = 'stock.move'

    bad_rate = fields.Float(digits=(4, 2), compute="_compute_bad_rate")

    @api.depends("picking_id.pack_operation_ids")
    @api.one
    def _compute_bad_rate(self):
        ops = self.picking_id.pack_operation_ids
        loc_id = self.env.ref("mrp_miaoyin.stock_location_bad_product").id
        if ops:
            bad_count = sum((op.qty_done for op in ops if op.location_dest_id.id == loc_id))
            self.bad_rate = float(bad_count) / self.product_uom_qty


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    # @api.multi
    # def do_new_transfer(self):
    #     for picking in self:
    #         super(StockPicking, picking).do_new_transfer()
    #         # if picking.move_lines_related:
    #         #     for move in picking.move_lines_related:
    #         #         move.bad_rate = 100.0


