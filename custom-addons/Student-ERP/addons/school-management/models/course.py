from odoo import models, fields

class Course(models.Model):
    _name = 'school.course'
    _description = 'Course'

    name = fields.Char(string='Course Name', required=True)
    code = fields.Char(string='Course Code', required=True)
    # description = fields.Text(string='Description')
    credits = fields.Integer(string='Credits', required=True)
    # duration = fields.Integer(string='Duration (weeks)', required=True)
    status = fields.Selection([
        ('active', 'Active'),
        ('inactive', 'Inactive'),
    ], string='Status', default='active', required=True)