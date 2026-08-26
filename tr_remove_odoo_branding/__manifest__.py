{
    'name': 'Remove Powered by Odoo',
    'version': '19.0.1.0.0',
    'category': 'Website',
    'summary': 'Remove & Replace Powered by Odoo from Website, Portal and Email Templates',
    'description': """
Remove Powered by Odoo — by Vayu Sharma
============================================
Hides or replaces all "Powered by Odoo" branding from:

- Website footer
- Customer & Vendor Portal
- Email notification templates
- Login page

Configure your own brand name and URL from Settings.
    """,
    'author': 'Vayu Sharma',
    'website': '',
    'license': 'OPL-1',
    'depends': ['portal', 'mail', 'website', 'base_setup'],
    'data': [
        'views/res_config_settings.xml',
        'views/remove_portal_branding.xml',
        'views/remove_email_branding.xml',
        'views/remove_website_branding.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            'tr_remove_odoo_branding/static/src/css/hide_branding.css',
        ],
        'web.assets_backend': [
            'tr_remove_odoo_branding/static/src/css/hide_branding.css',
        ],
    },
    'images': ['static/description/banner.png'],
    'installable': True,
    'application': False,
    'auto_install': False,
    'price': 5.00,
    'currency': 'USD',
}
