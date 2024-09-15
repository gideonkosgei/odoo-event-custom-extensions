# -*- coding: utf-8 -*-
{
    'name': 'Event Custom Extensions',
    'version': '1.0',
    'summary': 'Events Custom Extensions',
    'description': """
        This module extends the Odoo Events module Capabilities.
    """,
    'category': 'Event',
    'author': 'Gideon Kosgei',
    'depends': ['base', 'event'],
    'data': [
        # 'security/ir.model.access.csv',
        'views/event_views.xml',
        'views/event_ticket_template.xml'
    ],
    'installable': True,
    'application': False,
}
