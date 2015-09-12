{
    'name': "mrp miaoyin",
    'version': '1.0',
    'depends': ['mrp', 'stock', 'mail'],
    'author': "wangting",
    'category': 'custom',
    'data': [
        'data/product_category.xml',
        # 'views/offcut_production_view.xml',
        'data/stock_location_data.xml',
        'data/stock_route_data.xml',
        'views/mrp_routing_view.xml',
        'views/stock_move.xml',
        'views/bom_view.xml',
        'views/picking.xml',
        'views/production_record.xml'
    ],
    'application': False,
    'description': """
        mrp miaoyin 3.0
    """
}
