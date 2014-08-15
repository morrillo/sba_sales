from openerp.osv import osv,fields
from datetime import date

class product_language(osv.osv):
	_name = "product.language"
	_description = "Lenguaje del producto"

	_columns = {
		'name': fields.char('Name',size=32),
		}
product_language()

class product_familia(osv.osv):
	_name = "product.familia"
	_description = "Familia a la que pertenece el producto"

	_columns = {
		'name': fields.char('Name',size=32),
		}
product_familia()

class product_categoria(osv.osv):
	_name = "product.categoria"
	_description = "Categoria a la que pertenece el producto"

	_columns = {
		'name': fields.char('Name',size=32),
		}
product_categoria()

class product_version(osv.osv):
	_name = "product.version"
	_description = "Version a la que pertenece el producto"

	_columns = {
		'name': fields.char('Name',size=32),
		}
product_version()

class product_subcategoria(osv.osv):
	_name = "product.subcategoria"
	_description = "SubCategoria a la que pertenece el producto"

	_columns = {
		'name': fields.char('Name',size=32),
		}
product_subcategoria()

class product_product(osv.osv):
	_name = "product.product"
	_inherit = "product.product"

	def _fnct_pricelist_price(self, cr, uid, ids, field_name, args, context=None):
        	product_pricelist_obj = self.pool.get('product.pricelist')

	        if context is None:
        	    context = {}
	        res = {}
        	for product in self.browse(cr, uid, ids, context=context):
	            res[product.id] = self.pool.get('product.pricelist').price_get(cr,uid,[1],product.id,1.0,1,{'uom':1,'date':date.today()})[1]
        	return res

	def _fnct_pricelist_price_distrib(self, cr, uid, ids, field_name, args, context=None):
        	product_pricelist_obj = self.pool.get('product.pricelist')

	        if context is None:
        	    context = {}
	        res = {}
        	for product in self.browse(cr, uid, ids, context=context):
	        	res[product.id] = self.pool.get('product.pricelist').price_get(cr,uid,[12],product.id,1.0,1,{'uom':1,'date':date.today()})[12]
        	return res

	def _fnct_pricelist_price_librerias(self, cr, uid, ids, field_name, args, context=None):
        	product_pricelist_obj = self.pool.get('product.pricelist')

	        if context is None:
        	    context = {}
	        res = {}
        	for product in self.browse(cr, uid, ids, context=context):
	        	res[product.id] = self.pool.get('product.pricelist').price_get(cr,uid,[9],product.id,1.0,1,{'uom':1,'date':date.today()})[9]
        	return res

	def _fnct_pricelist_price_iglesias(self, cr, uid, ids, field_name, args, context=None):
        	product_pricelist_obj = self.pool.get('product.pricelist')

	        if context is None:
        	    context = {}
	        res = {}
        	for product in self.browse(cr, uid, ids, context=context):
	        	res[product.id] = self.pool.get('product.pricelist').price_get(cr,uid,[14],product.id,1.0,1,{'uom':1,'date':date.today()})[14]
        	return res


	_columns = {
		'events_ids': fields.many2many('product.event','product_event_rel','product_id','event_id','Eventos'),
		'familia': fields.many2one('product.familia','Familia'),
		'categoria': fields.many2one('product.categoria','Categoria'),
		'version': fields.many2one('product.version','Version'),
		'product_language': fields.many2one('product.language','Idioma'),
		'subcategoria': fields.many2one('product.subcategoria','SubCategoria'),
		'sba_sku_no': fields.char('Codigo SBU',size=32),
		'sba_code': fields.char('Codigo SBA',size=32),
		'product_origin': fields.selection((('Propio','Propio'),('Terceros','Terceros')),'Origen del producto'),
        	'pricelist_price': fields.function(_fnct_pricelist_price, string='Precio LP'),
        	'pricelist_price_distrib': fields.function(_fnct_pricelist_price_distrib, string='Precio Distribuidores'),
        	'pricelist_price_librerias': fields.function(_fnct_pricelist_price_librerias, string='Precio Librerias'),
        	'pricelist_price_iglesias': fields.function(_fnct_pricelist_price_iglesias, string='Precio Iglesias'),
		#'familia': fields.selection((('BIBLIAS','BIBLIAS'),('LIBROS','LIBROS'),('SELECCIONES NL','SELECCIONES NL'),\
		#	('SELECCIONES','SELECCIONES'),('PORCIONES NL','PORCIONES NL'),('PORCIONES','PORCIONES'),('NT','NT'),\
		#	('MEDIA','MEDIA'),('OTROS','OTROS')),'Familias'),
		#'categoria': fields.selection((('ACADEMICO','ACADEMICO'),('LUJO','LUJO'),('MISIONERA','MISIONERA'),('PRECIO MEDIO','PRECIO MEDIO'),\
		#		('LIBROS','LIBROS'),('EDUC DIFUSION','EDUC DIFUSION'),('JUEGOS','JUEGOS'),('MUSICA','MUSICA'),('REPLICA','REPLICA'),\
		#		('VARIOS','VARIOS'),('SELECCION','SELECCION')),'Categoria'),
		#'version': fields.selection((('Dios Habla Hoy','Dios Habla Hoy'),
		#			     ('Dios Habla Hoy con Deutero','Dios Habla Hoy con Deutero'),
		#			     ('Nueva Version Internacional','Nueva Version Internacional'),
		#			     ('Reina Valera 1909','Reina Valera 1909'),
		#			     ('Reina Valera 1960','Reina Valera 1960'),
		#			     ('Reina Valera 1995','Reina Valera 1995'),
		#			     ('Reina Valera Contemporanea','Reina Valera Contemporanea'),
		#			     ('Traduccion Lenguaje Actual','Traduccion Lenguaje Actual'),
		#			     ('Traduccion Lenguaje Actual con Deutero','Traduccion Lenguaje Actual con Deutero'),
		#			     ('Multiversion','Multiversion'),
		#			     ('Ninguna','Ninguna')),'Version'),
		#'subcategoria': fields.selection((('Digital','Digital'),('Especializado','Especializado'),\
		#				 ('Especializado-Jovenes','Especializado-Jovenes'),('Especializado-Mujeres','Especializado-Mujeres'),\
		#				 ('Estandar','Estandar'),('Estandar Economico','Estandar Economico'),\
		#				 ('Estandar-Letra Grande','Estandar-Letra Grande'),('Estudio','Estudio'),\
		#				 ('Ninios','Ninios')),'Sub-Categoria'),
		}

		#'familia': fields.selection((('BIBLIAS','BIBLIAS'),('LIBROS','LIBROS'),('SELECCIONES NL','SELECCIONES NL'),\
		#	('SELECCIONES','SELECCIONES'),('PORCIONES NL','PORCIONES NL'),('PORCIONES','PORCIONES'),('NT','NT'),\
		#	('MEDIA','MEDIA'),('OTROS','OTROS')),'Familias'),
		#	}
		# 'categoria': fields.selection((('ACADEMICO','ACADEMICO'),('LUJO','LUJO'),('MISIONERA','MISIONERA'),('PRECIO MEDIO','PRECIO MEDIO'),\
		#		('LIBROS','LIBROS'),('EDUC DIFUSION','EDUC DIFUSION'),('JUEGOS','JUEGOS'),('MUSICA','MUSICA'),('REPLICA','REPLICA'),\
		#		('VARIOS','VARIOS'),('SELECCION','SELECCION')),'Categoria'),
	
product_product()


class product_event(osv.osv):
	_name = "product.event"

	_columns = {
		'name': fields.char("Name"),
		'fecha_desde': fields.date('Fecha desde'),
		'fecha_hasta': fields.date('Fecha hasta'),
		'product_ids': fields.many2many('product.product','product_event_rel','event_id','product_id','Productos'),
		}


product_event()