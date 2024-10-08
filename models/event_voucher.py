# -*- coding: utf-8 -*-
try:
    import qrcode
except ImportError:
    qrcode = None
try:
    import base64
except ImportError:
    base64 = None

from io import BytesIO
from odoo import models, fields, api

class EventVoucher(models.Model):
    _name = 'event.voucher'
    _description = 'Event Voucher'
    _inherit = ["mail.thread", "mail.activity.mixin"]

    registration_id = fields.Many2one('event.registration', string='Registration')
    qr_code = fields.Binary('QRcode', compute="_generate_qr")

    token_food = fields.Boolean('Food', tracking=True)
    token_drink1 = fields.Boolean('Drinks(3)', tracking=True)
    token_drink2 = fields.Boolean('Drinks(3)', tracking=True)
    state = fields.Selection([('Open', 'Open'), ('Closed', 'Closed')], string='state', default='Open',
                             compute='_compute_state')
    name = fields.Char('Name', related='registration_id.name')
    email = fields.Char('Email', related='registration_id.email')
    barcode = fields.Char('Barcode', related='registration_id.barcode',store=True)


    def _generate_qr(self):
        for rec in self:
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=5,
                border=6,
            )

            base_url = self.env['ir.config_parameter'].get_param('web.base.url')
            # base_url = 'http://109.74.196.59:8069'
            # base_url = 'http://localhost:8069'

            qr_data = f'{base_url}/web/barcode_search?barcode={rec.barcode}'
            qr.add_data(qr_data)
            qr.make(fit=True)
            img = qr.make_image()

            # Save QR code image to BytesIO and encode it to base64
            temp = BytesIO()
            img.save(temp, format="PNG")
            qr_image = base64.b64encode(temp.getvalue())
            rec.qr_code = qr_image


    @api.depends('token_food', 'token_drink1', 'token_drink2')
    def _compute_state(self):
        for rec in self:
            if all([rec.token_food, rec.token_drink1, rec.token_drink2]):
                rec.state = 'Closed'
            else:
                rec.state = 'Open'


