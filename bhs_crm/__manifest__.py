# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'CRM Lead Code',
    'version': '1.0',
    'category': 'Sales/CRM',
    'sequence': 340,
    'author': 'Bac Ha Software',
    'summary': """
        Module allows automatically generate customer codes and classify customers and internal contacts.
    """,
    'description': """
        A product of Bac Ha Software allows automatically generate customer codes and classify customers and internal contacts.
    """,
    'website': 'https://bachasoftware.com/',
    'depends': ['hr', 'crm', 'account'],
    'data': [
        'data/ir_sequence_data.xml',
        'views/bh_crm_lead_code.xml'
    ],
    'images': ['static/description/banner.gif'],
    'installable': True,
    'auto_install': False,
    'application': True,
    'assets': {},
    'license': 'LGPL-3'
}
