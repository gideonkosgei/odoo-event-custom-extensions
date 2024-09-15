from odoo import models, fields

class EventEvent(models.Model):
    _inherit = 'event.event'
    event_url = fields.Char('Event URL', help="URL stored in the QR code")


