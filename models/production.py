from openerp import models, fields, api, exceptions, _


class Routing(models.Model):
    _inherit = 'mrp.routing'


    location_dest_id = fields.Many2one('stock.location')


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


