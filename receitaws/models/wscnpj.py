from odoo import models, fields, api

class receitaws(models.Model):
     _name = 'receitaws.receitaws'

     name = fields.Char()
     value = fields.Integer()
     value2 = fields.Float(compute="cnpj_cpf", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
     def cnpj_cpf(self):
         self.value2 = float(self.value) / 100
