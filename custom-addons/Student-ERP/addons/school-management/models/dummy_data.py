from odoo import models, fields
from odoo.modules.module import get_module_resource
import json
import random
from datetime import date, timedelta

class DummyDataGenerator(models.TransientModel):
    _name = 'school.dummy.generator'
    _description = 'Generate Dummy Data'

    def _load_json(self, filename):
        # filename example: 'students.json' or 'courses.json'
        path = get_module_resource('school-management', 'data', filename)
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)

    def generate_dummy_data(self):
        Student = self.env['school.student']
        Course = self.env['school.course']
        Enrollment = self.env['school.enrollment']
        Fee = self.env['school.fee']

        courses_data = self._load_json('courses.json')
        students_data = self._load_json('students.json')

        # Create courses
        courses = []
        for c in courses_data:
            courses.append(Course.create({
                'name': c['name'],
                'code': c['code'],
                'credits': c.get('credits', 3),
                'status': 'active',
            }))

        # Create students
        students = []
        for idx, s in enumerate(students_data, start=1):
            students.append(Student.create({
                'full_name': s['name'],
                'gender': s['gender'],
                'date_of_birth': date(2000, 1, 1) + timedelta(days=idx * 250),
                'email': f"{s['name'].lower().replace(' ', '.')}{idx}@test.com",
                'phone_number': f"9000{idx:04}",
                'addmission_date': date.today(),  # keep your field name
                'status': 'active',
            }))

        # Enroll students + add fees
        for student in students:
            course = random.choice(courses)
            Enrollment.create({
                'student_id': student.id,
                'course_id': course.id,
                'status': 'enrolled',
            })

            Fee.create({
                'student_id': student.id,
                'amount': random.choice([1000, 2000, 3000]),
                'fee_type': 'tuition',
                'status': random.choice(['paid', 'pending']),
                'due_date': date.today() + timedelta(days=30),
            })

        return True 
