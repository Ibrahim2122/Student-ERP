from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Enrollment(models.Model):
    _name = 'school.enrollment'
    _description = 'Enrollment'

    student_id = fields.Many2one('school.student', string='Student', required=True)
    course_id = fields.Many2one('school.course', string='Course', required=True)
    enrollment_date = fields.Date(string='Enrollment Date')
    status = fields.Selection([
        ('enrolled', 'Enrolled'),
        ('completed', 'Completed'),
        ('dropped', 'Dropped'),
    ], string='Status', default='enrolled')

    @api.constrains('student_id', 'course_id')
    def _check_duplicate_enrollment(self):
        for record in self:
            if record.student_id:
                # Logic to check if the student is already enrolled in the course
                existing = self.search([
                    ('student_id', '=', record.student_id.id),
                    ('course_id', '=', record.course_id.id),
                    ('id', '!=', record.id)
                ])
                if existing:
                    raise ValidationError("The student is already enrolled in this course.")