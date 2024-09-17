from odoo import models, fields, api
from odoo.exceptions import ValidationError


class EventRegistration(models.Model):
    _inherit = 'event.registration'

    @api.model
    def create(self, vals):

        # Email domain check
        user_email = vals.get('email')
        if not user_email or not user_email.endswith('@cgiar.org'):
            raise ValidationError("Only CGIAR email addresses are allowed to register.")

        # Existing registration check
        user_email = vals.get('email')
        event_id = vals.get('event_id')
        if not user_email:
            return super(EventRegistration, self).create(vals)

        existing_registration = self.search([
            ('email', '=', user_email),
            ('event_id', '=', int(event_id))
        ])

        if existing_registration:
            raise ValidationError(
                "This email has already been used to register for this event. Please check your mailbox for the confirmation and ticket")
        return super(EventRegistration, self).create(vals)
