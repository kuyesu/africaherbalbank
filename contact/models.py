from django.db import models
from wagtailstreamforms.blocks import WagtailFormBlock
from wagtailstreamforms.models.abstract import AbstractFormSetting

from django.utils.translation import gettext_lazy as _

from wagtail.core import blocks
from wagtail.core.models import Page

from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.core.fields import RichTextField, StreamField

# Create your models here.
class ContactPage(Page):
    banner_title = models.CharField(max_length=45, null=True, blank=False)
    banner_subtitle = models.CharField(max_length=45, null=True, blank=False)
    
    banner_image = models.ForeignKey(
        "wagtailimages.Image",
        verbose_name=_("Banner Image"),
        blank=False,
        null=True,
        on_delete=models.SET_NULL,
        related_name="+"
    )
    intro = RichTextField(blank=True)
    email = RichTextField(null=True, blank= False, features=["link"])
    Phone = RichTextField(null=True, blank= False,features=["link"])
    contact_person = RichTextField(null=True, blank= False,features=["link"])
    
    body = StreamField([
        ('paragraph', blocks.RichTextBlock()),
        ('form', WagtailFormBlock()),
    ],
    null=True,
    blank=True,)
    content_panels = Page.content_panels + [
        ImageChooserPanel("banner_image"),
        FieldPanel("banner_subtitle"),
        FieldPanel("banner_title"),
        FieldPanel('intro'),
        FieldPanel('email'),
        FieldPanel('Phone'),
        FieldPanel('contact_person'),
        StreamFieldPanel('body'),
        
    ]
    


class AdvancedFormSetting(AbstractFormSetting):
    to_address = models.EmailField()
