# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'School Management',
    'version': '1.0',
    'summary': 'School Management System',
    'sequence': 10,
    'description': """
School management module to manage students, courses, and teachers.
===========================================================""",
    'category': 'School Management/School Management',
    'website': 'https://ibrahimdev.cloud',
    'author': 'Ibrahim Baatiah & Samia Busaid',
    'depends': [],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/student_views.xml',
        'views/course_views.xml',
        'views/enrollment_views.xml',
        'views/fee_views.xml',
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'assets': {},
    'license': 'LGPL-3',
}
