# -*- coding: utf-8 -*-
from odoo import http

# class CheckDuplicateUser(http.Controller):
#     @http.route('/check_duplicate_user/check_duplicate_user/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/check_duplicate_user/check_duplicate_user/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('check_duplicate_user.listing', {
#             'root': '/check_duplicate_user/check_duplicate_user',
#             'objects': http.request.env['check_duplicate_user.check_duplicate_user'].search([]),
#         })

#     @http.route('/check_duplicate_user/check_duplicate_user/objects/<model("check_duplicate_user.check_duplicate_user"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('check_duplicate_user.object', {
#             'object': obj
#         })