from django.db import models

# Create your models here.
from django.db import models
from wagtail.core.blocks.struct_block import StructBlock
from wagtail.core.models import Page

from wagtail.images.blocks import ImageChooserBlock
from wagtail.core.fields import StreamField
from wagtail.admin.edit_handlers import StreamFieldPanel, FieldPanel
# Create your models here.
from streams import blocks


class Help(Page):
    """Landing page for about us"""
    template = "helpcenter/help.html"
    #  template = "about/about_us.html"
    subpage_types = []
    parent_page_types = ['home.HomePage']
    from wagtail.core import blocks
    
    body = StreamField(
        
        [
            ("heading", blocks.CharBlock(form_classname="Full Title")),
            ("Paragraph", blocks.RichTextBlock()),
            ("Immage", ImageChooserBlock()),
        ]
    )
    
    content_panels = Page.content_panels + [
        StreamFieldPanel("body")
    ]
    # class Meta: 
    #     template = "helpcenter/help.html"
    #     #  template = "about/about_us.html"
    #     subpage_types = []
    #     parent_page_types = ['home.HomePage']
    
    


class Faq(Page):
    """Landing page for about us"""
    template = "helpcenter/faq.html"
    subpage_types = []
    parent_page_types = ['home.HomePage']
    
    heading = models.CharField(blank=False, null=True, max_length=100)
    
    common_questions = StreamField(
        [
            ("commonly_asked_questions", blocks.FaqCard()),
            
        ],
        blank=False,
        null=True,
    )
    
    question_form = StreamField(
        [
            ("add_form", blocks.FormCard()),
        ],
        blank=False,
        null=True,
    )
    
    
    
    content_panels = Page.content_panels + [
        FieldPanel("heading"),
        StreamFieldPanel("common_questions"),
        StreamFieldPanel("question_form")
        
    ]
    
    # class Meta:
    #     template = "helpcenter/help.html"
    #     #  template = "about/about_us.html"
    #     subpage_types = []
    #     parent_page_types = ['home.HomePage']
    