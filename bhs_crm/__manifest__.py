# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'CRM Lead Code',
    'version': '1.0',
    'category': 'Sales/CRM',
    'sequence': 340,
    'summary': """
        Module allows to distinguish between customer lists and internal accounts.
    """,
    'description': """
        A product of Bac Ha Software allows to distinguish between customer lists and internal accounts.
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
