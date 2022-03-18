from odoo import _, api, fields, models
from odoo.exceptions import ValidationError

class RestPosting(models.Model):
    _name = 'rest.post'

    
    description = fields.Text(string='Description', size = 140, required=True,)

    @api.constrains('description')
    def constrain_description(self):
        """Raises a validation error if the post are
         longer then 500 character"""
        if self and len(self.description) > 500:
            raise ValidationError("You can not post more then 500 characters")
