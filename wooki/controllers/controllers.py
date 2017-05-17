# -*- coding: utf-8 -*-
from odoo import http

# class Wooki(http.Controller):
#     @http.route('/wooki/wooki/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/wooki/wooki/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('wooki.listing', {
#             'root': '/wooki/wooki',
#             'objects': http.request.env['wooki.wooki'].search([]),
#         })

#     @http.route('/wooki/wooki/objects/<model("wooki.wooki"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('wooki.object', {
#             'object': obj
#         })