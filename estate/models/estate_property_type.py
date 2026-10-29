from odoo import fields, models


class EstatePropertyType(models.Model):
    _name = 'estate.property.type'
    _description = 'Property Type'

    name = fields.Char(string='Name', required=True)

    _check_name = models.Constraint(
        'UNIQUE(name)',
        'The property type name must be unique.',
    )
