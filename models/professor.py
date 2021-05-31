# -*- coding: utf-8 -*-

from odoo import models, fields, api

class UniversityProfessor(models.Model):
     _name = 'university.professor'
     _description = 'university.professor'
     _rec_name = 'f_name'

     f_name = fields.Char(string='First name')
     l_name = fields.Char(string='Last name')
     sexe = fields.Selection([('male', 'Male'), ('female', 'Female')])
     identity_card = fields.Char(string='Identity card')
     adresse = fields.Text(string='Adresse')
     birthday = fields.Date(string='Birthday', default=fields.Datetime.now())
     start_date = fields.Datetime(string='Start Date', default=fields.Datetime.now())
     email = fields.Char()
     phone = fields.Char()
     image_1920 = fields.Binary(string="Upload professor image")

     state = fields.Selection(string="State", selection=[
          ('draft', 'Draft'),
          ('confirm', 'Confirmed'),
          ('cancel', 'Cancelled'),
     ], required=False, default='draft')

     department_id = fields.Many2one(comodel_name='university.department')
     subject_id = fields.Many2one(comodel_name='university.subject')
     #classroom_id = fields.Many2one(comodel_name='university.classroom')
     classroom_ids = fields.Many2many(comodel_name='university.classroom',
                                      relation='prof_class_rel',
                                      column1='f_name',
                                      column2='classroom_name')

     def btn_draft(self):
          self.state = 'draft'

     def btn_confirm(self):
          self.state = 'confirm'

     def btn_cancel(self):
          self.state = 'cancel'

     #filtre entre les 2 selection Many2one
     @api.onchange('department_id')
     def onchange_department_id(self):
          for rec in self:
               return {'domain': {'subject_id': [('department_id', '=', rec.department_id.id)]}}