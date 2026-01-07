from odoo import models, fields, api
from datetime import date

class Student(models.Model):
    _name = 'school.student'
    _description = 'Student'
    _rec_name = 'full_name'

    # id = fields.Integer(string='ID', required=True)
    full_name = fields.Char(string='Name', required=True)
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
    ], string='Gender', required=True)
    date_of_birth = fields.Date(string='Date of Birth' , required=True)
    email = fields.Char(string='Email')
    phone_number = fields.Char(string='Phone Number')
    address = fields.Text(string='Address')
    addmission_date = fields.Date(string='Admission Date', required=True)
    status = fields.Selection([
        ('active', 'Active'),
        ('inactive', 'Inactive'),
        ('graduated', 'Graduated'),
    ], string='Status', default='active', required=True)
    
    # course_ids = fields.Many2many('school.course', string='Courses')

    age = fields.Integer(string='Age', compute='_compute_age', store=True)

    @api.depends('date_of_birth')
    def _compute_age(self):
        today = date.today()
        for rec in self:
            if rec.date_of_birth:
                rec.age = (today - rec.date_of_birth).days // 365
            else:
                rec.age = 0