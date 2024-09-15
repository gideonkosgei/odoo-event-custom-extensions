# -*- coding: utf-8 -*-
# from odoo import http


# class EventCustomExtensions(http.Controller):
#     @http.route('/event_custom_extensions/event_custom_extensions', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/event_custom_extensions/event_custom_extensions/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('event_custom_extensions.listing', {
#             'root': '/event_custom_extensions/event_custom_extensions',
#             'objects': http.request.env['event_custom_extensions.event_custom_extensions'].search([]),
#         })

#     @http.route('/event_custom_extensions/event_custom_extensions/objects/<model("event_custom_extensions.event_custom_extensions"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('event_custom_extensions.object', {
#             'object': obj
#         })

