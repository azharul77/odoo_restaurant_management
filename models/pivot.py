from odoo import models, fields, api, _


class ProjectTaskDetails(models.Model):
    _name = "project.task.details"
    _auto = False

    project = fields.Many2one('project.project')
    partner = fields.Many2one('res.partner', string='Customer')
    date_deadline = fields.Char(string='Deadline Date')

    def init(self):
        self._cr.execute(""" 
           CREATE OR REPLACE VIEW project_task_details AS ( 
               SELECT 
                 row_number() OVER () as id,
                 ps.project_id as project,  
                 ps.date_deadline as date_deadline,
                 aa.partner_id as partner
                FROM project_task ps 
                LEFT JOIN  project_project pp ON ps.project_id = pp.id
                LEFT JOIN  account_analytic_account aa ON pp.analytic_account_id = aa.id)
                
    """)
