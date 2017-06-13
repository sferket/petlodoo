# petl_odoo
Provide Odoo io functionality for petl

Example:  

	import petl as etl  
	from petl.util.base import Table  
	from petl_odoo.io.odoo import Odoo, fromodoo, toodoo  
	
	# Initialize connection to Odoo  
	odoo = Odoo('http://10.200.12.20:8069', 'test', 'admin', 'admin')  
	
	# Get data from Odoo  
	table1 = fromodoo(odoo, 'product.template', [], ['name', 'standard_price', 'create_date'])  
	print table1  
	
	# Remove columns from data set  
	table2 = etl.cutout(table1, 'standard_price', 'create_date')  
	print table2  
	
	# Rename all products in set  
	table3 = etl.convert(table2, 'name', lambda v: v+'(2)')  
	print table3  
	
	# Write set back to Odoo  
	toodoo(table3, odoo, 'product.template', batch=500, tracking_disable=True)  




