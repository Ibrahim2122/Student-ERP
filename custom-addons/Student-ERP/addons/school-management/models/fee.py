from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Fee(models.Model):
    _name = 'school.fee'
    _description = 'Fee Structure'

    student_id = fields.Many2one('school.student', string='Student', required=True, ondelete='cascade')
    amount = fields.Float(string='Amount', required=True)
    amount_display = fields.Char(compute="_compute_amount_display")
    fee_type = fields.Selection([
        ('tuition', 'Tuition Fee'),
        ('exam', 'Exam Fee'),
        ('misc', 'Misc Fee'),
    ], string='Fee Type', required=True)
    # currency_id = fields.Many2one('res.currency', default=lambda self: self.env.company.currency_id)
    due_date = fields.Date(string='Due Date')
    payment_date = fields.Date(string='Payment Date')
    status = fields.Selection([
        ('pending', 'Pending'),
        ('paid', 'Paid'),
    ], string='Status', default='pending', required=True)
    paid_state = fields.Selection([
        ('paid', 'Paid'),
        ('unpaid', 'Unpaid'),
], string='Paid State', compute='_compute_paid_state', store=True)

    notes = fields.Text(string='Notes')


    @api.constrains('amount')
    def _check_amount_positive(self):
        for record in self:
            if record.amount <= 0:
                raise ValidationError("The fee amount must be positive.")
            
    @api.onchange('status')
    def _onchange_status(self):
        if self.status == 'paid' and not self.payment_date:
            self.payment_date = fields.Date.today()
        elif self.status != 'paid':
            self.payment_date = False
    
    def _mark_as_paid(self):
        for record in self:
            record.status = 'paid'
            if not record.payment_date:
                record.payment_date = fields.Date.today()

    def _compute_amount_display(self):
        for rec in self:
            rec.amount_display = f"{rec.amount:,.2f} $"

    @api.depends('status')
    def _compute_paid_state(self):
        for rec in self:
            rec.paid_state = 'paid' if rec.status == 'paid' else 'unpaid'
