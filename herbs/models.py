# from django.db import models
# from wagtail.contrib.table_block.blocks import TableBlock
# from wagtail.core.models import Page
# from wagtail.admin.edit_handlers import FieldPanel

# # Create your models here.
# new_table_options = {
#     'minSpareRows': 0,
#     'startRows': 6,
#     'startCols': 4,
#     'colHeaders': False,
#     'rowHeaders': False,
#     'contextMenu': True,
#     'editor': 'text',
#     'stretchH': 'all',
#     'height': 216,
#     'language': 'en',
#     'renderer': 'text',
#     'autoColumnSize': False,
# }

# class HerbsDatabase(Page):
    
#     template  = "herbs/database.html"
    
#     table = TableBlock(table_options=new_table_options)
    
#     content_panels = Page.content_panels + [
#         FieldPanel("table"),
#     ]