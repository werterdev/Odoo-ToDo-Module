# -*- coding: utf-8 -*-


from odoo import models, fields

class TodoTask(models.Model):
    _name = 'todo.task'
    _description = 'To-Do Task'

    name = fields.Char(string="Titel", required=True)
    description = fields.Text(string='Beschreibung')
    effort = fields.Float(string="Aufwand in h", default="0")
    due_date = fields.Date(string='Fälligkeitsdatum', required=True)
    owner = fields.Many2one('res.users', string='Zugeteilt', index=True, tracking=True, default=lambda self: self.env.user)
    is_done = fields.Boolean(string='Erledigt', default=False)

    project_id = fields.Many2one("todo.project")