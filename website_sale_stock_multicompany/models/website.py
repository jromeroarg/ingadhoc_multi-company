##############################################################################
# For copyright and license notices, see __manifest__.py file in module root
# directory
##############################################################################

import logging
from odoo import models, tools
from odoo.http import request


class Website(models.Model):

    _inherit = 'website'


    def _get_warehouse_available(self):
        if self._context.get('company_fix'):
            company = self._context.get('company_fix')
            return (
                        self.env['ir.default'].get('sale.order', 'warehouse_id', company_id=company) or
                        self.env['stock.warehouse'].sudo().search([('company_id', '=', company)], limit=1).id
                )
        return super()._get_warehouse_available()
