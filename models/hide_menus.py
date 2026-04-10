# -*- coding: utf-8 -*-
from odoo import fields, models


class HideMenus(models.Model):
    _name = 'hide.menus'

    name = fields.Char(string="Name")
    customer_id = fields.Many2one(comodel_name='res.partner', string="Customer")