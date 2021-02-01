from odoo import models, fields, api


class İletişimSayfa(models.Model):
    _name = 'kh.contact'
    _description = 'İletişim Sayfası'
    _rec_name = 'name'


    name = fields.Char(string="Ad", readonly=True)
    surname = fields.Char(string="Soyad", readonly=True)
    date = fields.Date(string="Tarih", readonly=True)
    phone = fields.Char("Telefon", readonly=True)
    mail = fields.Char(string="Email", readonly=True)
    comment = fields.Text(string="Mesaj", readonly=True)
