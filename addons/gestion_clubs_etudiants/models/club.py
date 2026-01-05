from odoo import models, fields, api # type: ignore

class Club(models.Model):
    _name = "gestion.club"
    _description = "Club Étudiant"

    name = fields.Char(string="Nom du club", required=True)
    description = fields.Text(string="Description")
    date_creation = fields.Date(string="Date de création")
    responsable_id = fields.Many2one("gestion.etudiant", string="Responsable du club")
    nb_etudiants = fields.Integer(string="Nombre d'étudiants",compute="_compute_nb_etudiants"
    )
    @api.depends('name')
    def _compute_nb_etudiants(self):
        for club in self:
            club.nb_etudiants = self.env['gestion.etudiant'].search_count([
                ('club_id', '=', club.id)
            ])