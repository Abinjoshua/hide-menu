# -*- coding: utf-8 -*-
from odoo import models


class IrUiMenu(models.Model):
    _inherit = "ir.ui.menu"

    def _visible_menu_ids(self, debug=False):
        all_menus = super()._visible_menu_ids()
        print(all_menus)

        to_hide_menu = self.env.user.hide_menus
        print(to_hide_menu)
        hidden = all_menus - set(to_hide_menu.ids)
        print(hidden)

        return hidden
