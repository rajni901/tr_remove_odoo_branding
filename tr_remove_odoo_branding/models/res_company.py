from odoo import api, fields, models


class ResCompany(models.Model):
    _inherit = 'res.company'

    custom_powered_by_name = fields.Char(
        string='Powered By Name',
        default='',
    )
    custom_powered_by_url = fields.Char(
        string='Powered By URL',
        default='',
    )


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    custom_powered_by_name = fields.Char(
        related='company_id.custom_powered_by_name',
        readonly=False,
        string='Brand Name',
    )
    custom_powered_by_url = fields.Char(
        related='company_id.custom_powered_by_url',
        readonly=False,
        string='Brand URL',
    )
