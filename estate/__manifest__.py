{
    'name': 'Real Estate',
    'version': '1.0',
    'author': 'Kishan',
    'category': 'Sales',
    'summary': 'Manage real estate properties and advertisements',
    'description': """
Real Estate Module
==================
A module to manage real estate properties, types, tags, and offers.
Developed following the Odoo Server Framework 101 tutorial.
    """,
    'depends': [
        'base',
    ],
    'data': [
        'security/ir.access.csv',
        'views/estate_property_views.xml',
        'views/estate_property_type_views.xml',
        'views/estate_property_tag_views.xml',
        'views/estate_property_offer_views.xml',
        'views/estate_menus.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
