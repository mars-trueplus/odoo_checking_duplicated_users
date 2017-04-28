# -*- coding: utf-8 -*-

from odoo import models, fields, api

class User(models.Model):
    _inherit = 'res.users'

    @api.onchange('login')
    def _unique_username_onchange(self):
        username = self.login
        # search username in database and check unique
        user = self.search([('login', '=', username)])
        if user:
            return {
                'warning': {
                    'title': 'Unique username',
                    'message': 'You can not have two users with the same login !'
                }
            }
