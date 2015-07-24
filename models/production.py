from openerp import models, fields, api, exceptions, _


class Routing(models.Model):
    _inherit = 'mrp.routing'

    location_dest_id = fields.Many2one('stock.location', required=True)


class Production(models.Model):
    _inherit = 'mrp.production'

    @api.one
    def _dest_id_default(self):
        if self.routing_id and self.routing_id.location_dest_id:
            return self.routing_id.location_dest_id.id
        return super(Production, self)._dest_id_default()

    location_dest_id = fields.Many2one(default=_dest_id_default,
                                       readonly=True)
    location_src_id = fields.Many2one(readonly=True)

    @api.onchange('routing_id')
    @api.one
    def _onchange_routing_id(self):
        if self.routing_id and self.routing_id.location_dest_id:
            self.location_dest_id = self.routing_id.location_dest_id

    # @api.one
    # def _compute_product_category_cutoff_id(self):
    #     self.product_category_cutoff_id = self.env.ref("mrp_miaoyin.product_category_offcut").id

    #product_category_cutoff_id = fields.Integer(compute=_compute_product_category_cutoff_id, store=True, readonly=True)

    #product_category_cutoff_id = fields.Integer(default=lambda self: self.env.ref("mrp_miaoyin.product_category_offcut").id,
    #                                            readonly=True)

    #product_id = fields.Many2one('product.product', domain=[('category_id', 'child_of', product_category_cutoff_id)])


class BomLine(models.Model):
    _inherit = 'mrp.bom.line'

    allowance = fields.Float()
