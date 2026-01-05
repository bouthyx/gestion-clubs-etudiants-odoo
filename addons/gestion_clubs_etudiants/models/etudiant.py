from odoo import models, fields # type: ignore

class Etudiant(models.Model):
    _name = "gestion.etudiant"
    _description = "Étudiant"

    name = fields.Char(string="Nom complet", required=True)
    email = fields.Char(string="Email")
    club_id = fields.Many2one("gestion.club", string="Club")
    date_adhesion = fields.Date(string="Date d’adhésion")