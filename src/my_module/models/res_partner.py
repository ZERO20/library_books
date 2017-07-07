#-*- coding: utf-8 -*-
from openerp import models, fields

class ResPartner(models.Model):
    """
    The One2many field attributes are as follows:
        *comodel_name: This is the target model identifier and is mandatory for all relational fields, but it can be defined position-wise without the keyword.
        *inverse_name: This applies only to One2many and is the field name in the target model for the inverse Many2one relation
        *limit: This applies to One2many and Many2many and sets an optional limit on the number of records to read that are used at the user interface level
    
    The Many2many field attributes are as follows:
        *comodel_name: (as defined earlier).
        *relation: This is the name to use for the table supporting the relation, overriding the automatically defined name.
        *column1: This is the name for the Many2one field in the relational table linking to this model.
        *column2: This is the name for the Many2one field in the relational table linking to the comodel
        
        The relation table's automatic name is <model1>_<model2>_rel for example library_book_res_partner_rel
    """
    _inherit = 'res.partner'
    book_ids = fields.One2many('library.book','publisher_id', string='Published Books')
    book_ids = fields.Many2many('library.book',
        string='Authored Books',
        #relation='library_book_res_partner_rel' #optional
        )

