# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'Restaurant Project ',
    'version' : '14.0.1.0',
    'summary': 'Restaurant Project will help me to learn odoo basics',
    'sequence': -101,
    'description': """Restaurant Project will help me to learn odoo basics""",
    'category': 'sale and Invoicing',
    'website': 'https://www.odoo.com/page/billing',
    'images' : ['images/accounts.jpeg','images/bank_statement.jpeg','images/cash_register.jpeg','images/chart_of_accounts.jpeg','images/customer_invoice.jpeg','images/journal_entries.jpeg'],
    'depends' : ['base', 'mail'],
    'data': ['security/ir.model.access.csv',
        'views/staff_view.xml',
        'views/menu_view.xml',
    ],
    # 'demo': [
    #     'demo/account_demo.xml',
    # ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
