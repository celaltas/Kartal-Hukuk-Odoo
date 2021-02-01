from odoo import models, fields, api


class Article(models.Model):
    _name = 'kh.article'
    _description = 'Makaleler'
    _rec_name = 'title'


    title = fields.Char(string="Başlık", required=True)
    content = fields.Text(string="İçerik", required=True)
    date = fields.Date(string="Tarih", required=True, default=fields.Date.today())
    faaliyetAlanlari_ids = fields.Many2many('kh.faaliyet', string="İlgili Alan(lar)",required=True)
