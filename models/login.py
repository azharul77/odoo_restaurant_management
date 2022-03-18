from odoo import _, api, fields, models

class RestaurantLog(models.Model):
    _name = 'rest.log'

    username = fields.Char(string='Username')
    password = fields.Char(string='Password')
    connected = fields.Boolean(string='Connected', default=False)

    def connect(self):
        self.ensure_one()
        self.update({'connected': True,})