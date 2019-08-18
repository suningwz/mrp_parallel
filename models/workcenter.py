# -*- coding: utf-8 -*-
from odoo import models, fields, api

#Add properties to the work center to allow folding by default in kanban and the crucial workcentertbc field for TBC warnings later.
@api.model
class workcenter(models.Model):
    _inherit = ['mrp.workcenter']

    fold = fields.Boolean(string='Fold in kanban')
    workcentertbc = fields.Boolean(string='TBC',required=False,help='',index=False)