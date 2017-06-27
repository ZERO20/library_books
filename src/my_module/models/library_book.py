#-*- coding: utf-8 -*-
from openerp import models, fields

class LibraryBook(models.Model):    
    """
    Char fields support a few specific attributes. As an example:
    short_name = fields.Char(string='Short Title',
                            size=100, # For Char only
                            translate=False, # also for Text fields)

    Fields types:
        Char for string values.
        Text for multi-line string values.
        Selection for selection lists. This has a list of values and description pairs. The value that is selected is what gets stored in the database, and it can be a string or an integer.
        Html is similar to the Text field, but is expected to store rich text in the HTML format.
        Binary fields store binary files, such as images or documents.
        Boolean stores True/False values.
        Date stores date values. The ORM handles them in the string format, but they are stored in the database as dates. The format used is defined in openerp.fields.DATE_FORMAT.
        Datetime for date-time values. They are stored in the database in a naive date time,in UTC time. The ORM represents them as a string and also in UTC time. The format used is defined in openerp.fields.DATETIME_FORMAT.
        Integer fields need no further explanation.
        Float fields store numeric values. The precision can optionally be defined with a total number of digits and decimal digits pairs.
        Monetary can store an amount in a certain currency; it is also explained in another recipe.

    A few fields are added by default in Odoo models, so we should not use these names for our fields.
    These are the id field, for the record's automatically generated identifier, and a few audit log fields, which are as follows:
        id for the record's automatically generated identifier
        create_date is the record creation timestamp
        create_uid is the user that created the record
        write_date is the last recorded edit timestamp
        write_uid is the user that last edited the record
        active it should be a Boolean flag allowing for mark records as inactive. By default is True.
    
    The automatic creation of these log fields can be disabled by setting the _log_access=False model attribute.
    """
    
    #Models have structural attributes defining their behavior.
    _name = 'library.book'
    _description = 'Library Book'#add a human-friendly title to the model.
    _order = 'date_release desc, name'#To have records sorted first by default from newer to older and then by title.
    _rec_name = 'short_name'

    name = fields.Char('Title',required = True, help='Help text example')
    short_name = fields.Char(string='Short Title',
    size=100, #For Char only
    translate=False, #also for Text fields
    )
    date_release = fields.Date('Release Date')
    author_ids = fields.Many2many('res.partner', string = 'Authors')
    notes = fields.Text('Internal Notes')
    state = fields.Selection(
        [
            ('draft', 'Not avaliable'),
            ('avaliable', 'Avaliable'),
            ('lost', 'Lost')
        ],'State'#ChoiceField
    )
    description = fields.Html(
        string='Desciption',
        #optional: 
        sanitize=True,#is used by HTML fields and strips its content from potentially insecure tags.
        strip_style=False,#is also an HTML field attribute and has the sanitization to also remove style elements.
        translate=False#when set to True, makes the field translatable; it can hold a different value depending on the user interface language.
        )
    cover = fields.Binary('Book Cover')
    out_of_print = fields.Boolean('Out of print?')
    date_updated = fields.Datetime('Last Updated')
    pages = fields.Integer(string='Number of pages',
        default=0, #It can also be a function that is used to calculate the default value. 
                    #For example, default=_compute_default, where _compute_ default is a method defined on the model before the field definition.
        help='Total book page count', #is an explanation text displayed in the UI tooltips.
        groups='base.group_user',#makes the field available only to some security groups.
        states={'cancel':[('readonly', True)]},#allows the user interface to dynamically set the value for the readonly, required, and invisible attributes, depending on the value of the state field.
        copy=True,#flags if the field value is copied when the record is duplicated.
        index=False,#when set to True, makes for the creation of a database index for the field, allowing faster searches
        readonly=False,#flag makes the field read-only by default in the user interface.
        required=False,#flag makes the field mandatory by default in the user interface.
        company_dependent=False
        )
    reader_rating = fields.Float('Reader Average Rating', (14,4)) #optional precision (total, decimals)

    def name_get(self):
        """
        This method must return a list of tuples with
        two elements: the ID of the record and the Unicode string representation for the record.
        """
        result = []        
        for record in self:
            print(fields.Date.from_string('2017-06-27'),' soy yo')
            result.append((record.id, "{} ({})".format(record.name, record.date_release)))
        return result