# -*- coding: utf-8 -*-
from odoo import fields, models


class ResUser(models.Model):
    _inherit = "res.users"

    hide_menus = fields.Many2many('ir.ui.menu',string="Hide Menus User Wise")