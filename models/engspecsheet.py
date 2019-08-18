# -*- coding: utf-8 -*-
from odoo import models, fields, api

#Model for EngineerSpecSheet to hold custom product BOM engineering job specification sheets.
@api.model
class engspecsheet(models.Model):
    _name = 'mrp_parallel.engspecsheet'
    _description = 'Engineering Spec Sheet'
    _inherit = ['mail.thread','mail.activity.mixin']

    name = fields.Char('Name', readonly=True, select=True, copy=False, default='New')
    revision = fields.Integer(string='Revision',default=1,track_visibility='onchange')
    description = fields.Text()
    attachment = fields.Binary(string='Attachment',attachment=True,required=True,track_visibility='onchange')
    store_fname = fields.Char(string='File Name')
    approved = fields.Boolean(string='Approved for manufacture',track_visibility='onchange')

    @api.model
    def create(self, vals):
        if vals.get('name', 'New') == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code('eng.sequence') or 'New'
        result = super(engspecsheet, self).create(vals)
        return result