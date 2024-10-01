# -*- coding: utf-8 -*-


from odoo import models, fields

class TodoProject(models.Model):
    _name = 'todo.project'
    _description = 'To-Do Projects'

    name = fields.Char(string="Titel", required=True)
    description = fields.Text(string='Beschreibung')
    effort = fields.Float(string="Aufwand in h", default="0")
    due_date = fields.Date(string='Fälligkeitsdatum', required=True)
    owner = fields.Many2one('res.users', string='Zugeteilt', index=True, tracking=True, default=lambda self: self.env.user)
    is_done = fields.Boolean(string='Erledigt', default=False)

    task_ids = fields.One2many("todo.task", "project_id", string="")