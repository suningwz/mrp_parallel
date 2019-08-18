## -*- coding: utf-8 -*-
#from odoo import models, fields, api

##Add an automated sequence field to uniquely identify opportunities
#@api.model
#class opportunity(models.Model):
#    _inherit = ['crm.opportunity']

#    oppnumber = fields.Char('Opp Number', readonly=True, select=True, copy=False, default='New')

#    @api.model
#    def create(self, vals):
#        if vals.get('oppnumber', 'New') == 'New':
#            vals['oppnumber'] = self.env['ir.sequence'].next_by_code('opportunity.sequence') or 'New'
#        result = super(opportunity, self).create(vals)
#        return result

#    @api.multi
#    def name_get(self):
#        res = super(opportunity, self).name_get()
#        data = self.oppnumber + ":" + self.oppnumber
#        return data
