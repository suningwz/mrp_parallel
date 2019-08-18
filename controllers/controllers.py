# -*- coding: utf-8 -*-
#from odoo import http

# class engineering(http.Controller):
#     @http.route('/engineering/engineering/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/engineering/engineering/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('engineering.listing', {
#             'root': '/engineering/engineering',
#             'objects': http.request.env['engineering.engineering'].search([]),
#         })

#     @http.route('/engineering/engineering/objects/<model("engineering.engineering"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('engineering.object', {
#             'object': obj
#         })