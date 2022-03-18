from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class RestStaff(models.Model):
    _name = 'rest.staff'
    _description = "This model will store the data of staff"
    _rec_name = 'name'
    _inherit = ['mail.thread', 'mail.activity.mixin']
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
# search method apply

    # def check_orm(self):
    #     search_var = self.env['rest.staff'].search(['|', ('status', '=', 'active'), ('gender', '=', 'male')])
    #     for rec in search_var:
    #         print("Full Name:############", rec.full_name, 'gender: $$$$$$$$$$', rec.gender)

# search count method apply

    # def check_orm(self):
    #     searchCount = self.env['rest.staff'].search_count([])
    #     print("Total Search Count: ######", searchCount)
# browser method apply

    # def check_orm(self):
    #     browse_var = self.env['rest.staff'].browse([12, 9])
    #     for rec in browse_var:
    #         print("Browse Var: ############", rec, "Name: ", rec.full_name, "age: ", rec.age, "gender: ", rec.gender)

# ref method apply
    # def check_orm(self):
    #     ref_var = self.env.ref('restaurant_project.rest_staff_form_view_id')
    #     print("Ref id: ##########", ref_var.model_data_id, "name: ", ref_var.name)

# create method apply

    # def check_orm(self):
    #     create_var = self.env['rest.staff'].create({
    #         "full_name": "Function Record",
    #         "age": 100,
    #         "mobile": '01761970239'
    #     })
    #     print("create_var##########3", create_var.id)

    # def check_orm(self):
    #     write_var = self.env['rest.staff'].browse(6)
    #     write_var.write({
    #         "full_name": "Test Write",
    #         "age": 88,
    #         "mobile": '01761970239'
    #     })

    def do_resign(self):
        for rec in self:
            rec.status = 'resigned'

    @api.constrains('age')
    def val_age(self):
        for rec in self:
            if rec.age <= 18:
                raise ValidationError(_(" The age must be above than 18"))

    name = fields.Char(string="Name", size=50, required=True, track_visibility='always')
    age = fields.Integer(string="Age")
    dob = fields.Date(string="DOB")
    mobile = fields.Char(string="Mobile", track_visibility='always')
    email = fields.Char(string="Email",  track_visibility='always')
    country_id = fields.Many2one('res.country', string="Country")
    country_ids = fields.Many2many('res.country', string="Countries")
    country_code = fields.Char(string="Country Code", related="country_id.code")
    staff_line_ids = fields.One2many('rest.staff.lines', 'connecting_field', string='Staff Line')
    sequence = fields.Integer(string="Seq.")
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string="Gender", default="male")
    status = fields.Selection([('active', 'Active'), ('resigned', 'Resigned')], string="Status", readonly=True,
                              default="active")
    image = fields.Binary(string="Image")
    hand_salary = fields.Float(string="In Hand Salary")
    epf_esi = fields.Float(string="EPF+ESI")
    ctc_salary = fields.Float(string="CTC", compute="calc_ctc")

    @api.depends('hand_salary', 'epf_esi')
    def calc_ctc(self):
        for record in self:
            ctc = 0
            if record.hand_salary:
                ctc = ctc + record.hand_salary
            if record.epf_esi:
                ctc = ctc + record.epf_esi
            record.ctc_salary = ctc


class RestStaffLine(models.Model):
    _name = 'rest.staff.lines'

    connecting_field = fields.Many2one('rest.staff', string='Staff ID')
    name = fields.Char(string="Name")
    product_id = fields.Many2one("product.product", string="Product")
    sequence = fields.Integer(string="Seq.")





