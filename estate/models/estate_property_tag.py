from odoo import fields, models


class EstatePropertyTag(models.Model):
    _name = 'estate.property.tag'
    _description = 'Property Tag'

    name = fields.Char(string='Name', required=True)

    _check_name = models.Constraint(
        'UNIQUE(name)',
        'The tag name must be unique.',
    )
