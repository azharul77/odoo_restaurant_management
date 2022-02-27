from odoo import models, fields

class RestStaff(models.Model):
    _name = 'rest.staff'
    _description = "This model will store the data of staff"
    _rec_name = 'full_name'
    _order = 'age desc'

    def new_fun(self):
        print("The button function is calling")

    def delete_one2many(self):
        for record in self:
            if record.staff_line_ids:
                record.staff_line_ids = [(5, 0, 0)]
                return {
                    'effect': {
                        'fadeout': 'slow',
                        'type': 'rainbow_man',
                        'message': 'Record had been deleted successfully'
                    }
                }

    def do_resign(self):
        for rec in self:
            rec.status = 'resigned'

    full_name = fields.Char(string="Name", size=50, required=True)
    age = fields.Integer(string="Age")
    dob = fields.Date(string="DOB")
    mobile = fields.Char(string="Mobile")
    email = fields.Char(string="Email")
    country_id = fields.Many2one('res.country', string="Country")
    country_ids = fields.Many2many('res.country', string="Countries")
    country_code = fields.Char(string="Country Code", related="country_id.code")
    staff_line_ids = fields.One2many('rest.staff.lines', 'connecting_field', string='Staff Line')
    sequence = fields.Integer(string="Seq.")
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string="Gender", default="male")
    status = fields.Selection([('active', 'Active'), ('resigned', 'Resigned')], string="Status", readonly=True,
                              default="active")
    image = fields.Binary(string="Image")


class RestStaffLine(models.Model):
    _name = 'rest.staff.lines'

    connecting_field = fields.Many2one('rest.staff', string='Staff ID')
    name = fields.Char(string="Name")
    product_id = fields.Many2one("product.product", string="Product")
    sequence = fields.Integer(string="Seq.")





