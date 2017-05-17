# -*- coding: utf-8 -*-
from odoo import http

# class Infoplex(http.Controller):
#     @http.route('/infoplex/infoplex/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/infoplex/infoplex/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('infoplex.listing', {
#             'root': '/infoplex/infoplex',
#             'objects': http.request.env['infoplex.infoplex'].search([]),
#         })

#     @http.route('/infoplex/infoplex/objects/<model("infoplex.infoplex"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('infoplex.object', {
#             'object': obj
#         })