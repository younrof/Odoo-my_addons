# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime

class UniversityStudent(models.Model):
     _name = 'university.student'
     _description = 'university.student'

     f_name = fields.Char(string='First name')
     l_name = fields.Char(string='Last name')
     sexe = fields.Selection([('male', 'Male'), ('female', 'Female')])
     identity_card = fields.Char(string='Identity card')
     adresse = fields.Text(string='Adresse')
     birthday = fields.Date(string='Birthday', default=fields.Datetime.now())
     registration_date = fields.Datetime(string='Date of inscription', default=fields.Datetime.now())
     email = fields.Char()
     phone = fields.Char()
     image_1920 = fields.Binary(string="Upload student image")

     state = fields.Selection(string="State", selection=[
          ('draft', 'Draft'),
          ('confirm', 'Confirmed'),
          ('cancel', 'Cancelled'),
     ], required=False, default='draft')

     department_id = fields.Many2one(comodel_name='university.department')
     classroom_id = fields.Many2one(comodel_name='university.classroom')

     subject_ids = fields.Many2many(related='classroom_id.subject_ids')

     def btn_draft(self):
          self.state = 'draft'

     def btn_confirm(self):
          self.state = 'confirm'

     def btn_cancel(self):
          self.state = 'cancel'

     #show fields require f_name and l_name
     def name_get(self):
          result = []
          for student in self:
               name = student.f_name
               result.append((student.id, name))
          return result

     #birthday > registration_date
     @api.constrains('registration_date', 'birthday')
     def check_date(self):
          if self.birthday > datetime.date(self.registration_date):
               return ValueError('The birthday must be inferior then the registration date')
