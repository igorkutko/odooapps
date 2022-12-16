from odoo import api, fields, models
from odoo.exceptions import ValidationError


class ResPartner(models.Model):
    _inherit = 'res.partner'

    email = fields.Char(copy=False)

    @api.constrains('email')
    def _check_email_unique(self):
        domain = [('email', '=', self.email)]
        msg = 'An another partner already has this e-mail!'
        if self.email and self.env['res.partner'].search_count(domain) > 1:
            raise ValidationError(msg)
