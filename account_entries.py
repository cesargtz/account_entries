# -*- coding: utf-8 -*-

from odoo import models, fields, api

class account_invoice_tons(models.Model):
    _inherit = 'account.move'

    active = fields.Boolean(default=True)
