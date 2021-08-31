from django.db import models

from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel
from wagtail.contrib.settings.models import BaseSetting, register_setting

# Create your models here.

@register_setting
class SocialMediaSettings(BaseSetting):
    facebook = models.URLField(blank=True, null=True, help_text="Facebook Link")
    twitter = models.URLField(blank=True, null=True, help_text="Twitter Link")
    whatsapp = models.URLField(blank=True, null=True, help_text="WhatsApp Link")
    youtube = models.URLField(blank=True, null=True, help_text="YouTube Link")
    instagram = models.URLField(blank=True, null=True, help_text="Instagram Link")
    
    panels = [
        MultiFieldPanel(
            [
                FieldPanel("facebook"),
                FieldPanel("twitter"),
                FieldPanel("whatsapp"),
                FieldPanel("youtube"),
                FieldPanel("instagram")
            ], heading = "Social Media Settings"
        )
    ]