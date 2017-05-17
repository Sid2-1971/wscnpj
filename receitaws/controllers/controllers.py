# -*- coding: utf-8 -*-
from odoo import http

# class Receitaws(http.Controller):
#     @http.route('/receitaws/receitaws/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/receitaws/receitaws/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('receitaws.listing', {
#             'root': '/receitaws/receitaws',
#             'objects': http.request.env['receitaws.receitaws'].search([]),
#         })

#     @http.route('/receitaws/receitaws/objects/<model("receitaws.receitaws"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('receitaws.object', {
#             'object': obj
#         })