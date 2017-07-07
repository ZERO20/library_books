#-*- coding: utf-8 -*-

from openerp import models, fields, api

class BookCategory(models.Model):
    """
        Model with the parent and child relations    
    """
    _name = 'library.book.category'
    
    #To enable the special hierarchy support, also add the fallowing: **
    _parent_store = True#**
    parent_left = fields.Integer(index=True)#**
    parent_right = fields.Integer(index=True)#**
    _parent_name = 'parent_id'#**the correct field name should be indicated
    
    name = fields.Char('Category')
    parent_id = fields.Many2one('library.book.category', 
        string='Parent Category',
        ondelete = 'restrict', #Must have ondelete set to either 'cascade' or 'restrict'
        index = True
        )
    child_ids = fields.One2many(
        'library.book.category',
        'parent_id',
        string = 'Child Categories'
        )

    @api.constrains('parent_id')
    def _check_hierarchy(self):
        if not self._check_recursion():
            raise models.ValidationError('Error! You cannot create recursive categories.')