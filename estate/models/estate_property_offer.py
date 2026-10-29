from odoo import api, fields, models


class EstatePropertyOffer(models.Model):
    _name = 'estate.property.offer'
    _description = 'Property Offer'

    price = fields.Float(string='Price')
    status = fields.Selection(
        selection=[
            ('accepted', 'Accepted'),
            ('refused', 'Refused'),
        ],
        string='Status',
        copy=False,
    )
    partner_id = fields.Many2one('res.partner', string='Partner', required=True)
    property_id = fields.Many2one('estate.property', string='Property', required=True)
    validity = fields.Integer(string='Validity (days)', default=7)
    date_deadline = fields.Date(
        string='Deadline',
        compute='_compute_date_deadline',
        inverse='_inverse_date_deadline',
    )

    @api.depends('create_date', 'validity')
    def _compute_date_deadline(self):
        for record in self:
            start_date = record.create_date.date() if record.create_date else fields.Date.today()
            record.date_deadline = fields.Date.add(start_date, days=record.validity)

    def _inverse_date_deadline(self):
        for record in self:
            start_date = record.create_date.date() if record.create_date else fields.Date.today()
            if record.date_deadline and start_date:
                record.validity = (record.date_deadline - start_date).days
            else:
                record.validity = 7
