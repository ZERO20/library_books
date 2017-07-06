# -*- coding: utf-8 -*-
{
    'name': 'Library Books',  # nombre del módulo
    'summary': "This is the subtitle with a one-line description.",  # muestra un subtitulo del módulo.
    'description': """This is the description""",  # descripción del módulo
    'author': 'Edgar de la Cruz',  # autor        
    'license': 'LGPL-3',#Tipo de licencia
    'website': 'www.test.com',  # dirección de documentación.
    'category':'Website',#categoría
    'version': '1.0',  # versión
    'depends': ['base','decimal_precision'],# dependencias, puede tener una lista de otros módulos requeridos. Odoo los instalará automáticamente cuando este módulo sea instalado.
    'data' : ['views/library_book.xml'],#vistas 
    'application': True, #If this is True, the module is listed as an application. Usually, this is used for the central module of a functional area.
    'auto_install': False, #If this is True, it indicates that this is a "glue" module, which is automatically installed when all its dependencies are installed.
    'installable' : True, #If this is True (the default value), it indicates that the module is available for installation.
}
