# -*- coding: utf-8 -*-
from odoo import models, fields, api

#Override default behaviour when grouping work orders by work center that normally hides empty 'stages' in kanban.
#Force showing all stages even empty ones.
#Also override the default readonly property on the worksheet field in the workorder to allow changing this later to the custom engspecsheet PDF.
@api.model
class workorder(models.Model):
    _inherit = ['mrp.workorder']
    
    def _read_group_stage_ids(self, stages, domain, order):
        stage_ids = self.env['mrp.workcenter'].search([])
        return stage_ids

    workcenter_id = fields.Many2one('mrp.workcenter', group_expand='_read_group_stage_ids', track_visibility='onchange')
    worksheet = fields.Binary(readonly=False)
    origin = fields.Char(related='production_id.origin',store=False)
    timelinecolour = fields.Selection(string='Timeline Colour',selection=[['Maroon','Maroon'],['Red','Red'],['Orange','Orange'],['Olive','Olive'],['Green','Green'],['Purple','Purple'],['Fuchsia','Fuchsia'],['Lime','Lime'],['Teal','Teal'],['Aqua','Aqua'],['Blue','Blue'],['Navy','Navy'],['Black','Black'],['Gray','Gray'],['Silver','Silver']])
    timelinenotes = fields.Text(string='Timeline Notes')