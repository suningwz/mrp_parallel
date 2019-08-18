# -*- coding: utf-8 -*-
{
    'name': "MRP Parallel Extension",

    'summary': """
        MRP parallel production work centers, engineering custom spec sheets, GANTT planner for MRP.
	""",

    'description': """
        Custom module to extend Odoo for MRP parallel production, unique custom production with engineering spec sheets to replace
        work sheets on work orders for custom/bespoke products. Adds GANTT timeline for planning work orders.
        Requires web_timeline for GANTT and mrp_production_request for splitting manufacturing orders received by sales before
        allocating to work center manually.
    """,

    'author': "Chris Mann",
    'website': "https://github.com/OCA/manufacture",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Manufacturing',
    'version': '12.0.1.0.0',

    # any module necessary for this one to work correctly
    # Note: Add crm if implementing opportunities, add mrp_production_request for splitting manufacturing orders/work orders
    'depends': ['base', 'mrp', 'base_automation', 'web_timeline', 'mrp_production_request'],

    # always loaded
    'data': [
        'data/ir_actions_server_data.xml',
        'data/ir_sequence_data.xml',
        'security/engspecsheet_security.xml',
        'security/ir.model.access.csv',
        'views/engspecsheet_views.xml',
        'views/mrp_workcenter_views.xml',
        'views/mrp_workorder_views.xml',
        'views/product_product_views.xml',
        'views/product_template_views.xml',
        'views/timeline_views.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}