# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'ToDo',
    'version': '1.0',
    'author': 'Muhammed Sapmaz',
    "license": "LGPL-3",
    'description': "This is a todo add-on.",
    'depends': [
        'base_setup',
    ],
    'data': [
        'security/ir.model.access.csv',        
        'views/todo_task_view.xml',
        'views/todo_project_view.xml',
        'views/todo_menu.xml'
    ],
    'application': True
}