# -*- coding: utf-8 -*-
from odoo import models, fields, api

#Internal testing: Link engspecsheet to the product.template model/view and show the related PDF.
@api.model
class product(models.Model):
    _inherit = ['product.template']

    engspecsheet = fields.Many2one('mrp_parallel.engspecsheet',string='Engineering Spec Sheet',track_visibility='onchange')
    worksheet = fields.Binary(string='Worksheet',related='engspecsheet.attachment',store=False)
