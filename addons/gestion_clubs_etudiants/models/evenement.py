from odoo import models, fields # type: ignore

class Evenement(models.Model):
    _name = "gestion.evenement"
    _description = "Événement du club"

    name = fields.Char(string="Nom de l’événement", required=True)
    date = fields.Date(string="Date")
    lieu = fields.Char(string="Lieu")
    club_id = fields.Many2one("gestion.club", string="Club", required=True)
    description = fields.Text(string="Description")
