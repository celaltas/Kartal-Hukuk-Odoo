from odoo import models, fields, api


class PersonelBilgileri(models.Model):
    _name = 'kh.avukat'
    _description = 'Personel'
    _rec_name = 'ad'

    image_1920 = fields.Image("İmage", max_width=512, max_height=512)
    unvan = fields.Char(string="Ünvan")
    ad = fields.Char(string="Ad")
    soyad = fields.Char(string="Soyad")
    baroSicilNo = fields.Char(string="Baro Sicil No")
    birlikSicilNo = fields.Char(string="Birlik Sicil No")
    yabanciDil = fields.Char(string="Yabancı Dil")
    universite = fields.Char(string="Üniversite")
    lise = fields.Char(string="Lise")
    fakulte = fields.Char(string="Fakülte")
    image_url = fields.Char("İmage Url")

    ozgecmis = fields.Text(string="Özgeçmiş")
    faaliyetAlanlari_ids = fields.Many2many('kh.faaliyet', string="Faaliyet Alanları")


class FaaliyetAlanlari(models.Model):
    _name = 'kh.faaliyet'
    _description = 'Faaliyetler Alanları'
    _rec_name = 'name'

    name = fields.Char(string="Faaliyet Alanları")
