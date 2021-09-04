from django.db import models

# Create your models here.
from django.db import models
from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.admin.edit_handlers import StreamFieldPanel, FieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel

from streams import blocks

# Create your models here.
class AboutPage(Page):

    template = "about/about_us.html"
    subpage_types = []
    parent_page_types = ['home.HomePage']
    
    banner_title = models.CharField(max_length=45, null=True, blank=False)
    banner_subtitle = models.CharField(max_length=45, null=True, blank=False)
    
    banner_image = models.ForeignKey(
        "wagtailimages.Image",
        blank=False,
        null=True,
        on_delete=models.SET_NULL,
        related_name="+"
    )
    
    about_us_cards = StreamField(
        [
            ("classic", blocks.ClassicCard(required=False)),
            ("works", blocks.Works()),
            ("events", blocks.UpConingEvents()),
            ("activities", blocks.Activities()),
            ("JumboBanner", blocks.JumboBanner()),
            ("smallbanner", blocks.SmallBanner()),
            ("Testimonies", blocks.Testimonies()),
            ("partners", blocks.Partners()),
            ("CardMessage", blocks.CardMessage()),
            ("Testimonies1", blocks.CardTestimonies()),
            ("CardWave", blocks.CardWave()),
            ("table", blocks.CardTable()),
            ("Cardlapping", blocks.CardLapping()),
            ("technologies", blocks.Technologies()),
            ("CardLightSmall", blocks.CardLightSmall()),
            ("CardSubscribe", blocks.CardSubscribe()),
            ("CardContact", blocks.CardContact()),
            ("CardTeam", blocks.CardTeam()),
            ("CardActivity", blocks.CardActivity()),
            ("CardLight", blocks.CardLight()),
            ("CardImage", blocks.CardImage()),
            ("CardGeneric", blocks.CardGeneric()),
            ("cta", blocks.CTABlock(required=False)),
            # ("classic", blocks.ClassicCard(required=False)),
            ("richtext", blocks.RichtextBlock()),
            ("simpletext", blocks.SimpleRichtextBlock()),
            # ("cta", blocks.CTABlock()),
            # ("buttonlogic", blocks.LinkStructValue()),
            ("cardBlock", blocks.CardBlock()),
            ("button", blocks.ButtonBlock()),
            ("titleandtext", blocks.TitleAndTextBlock()),
            ("sliding_images", blocks.SlidingImage()),
        ],
        null=True,
        blank=True,
        
    )
    
    
    content_panels = Page.content_panels + [
        
        FieldPanel("banner_title"),
        FieldPanel("banner_subtitle"),
        ImageChooserPanel("banner_image"),
        StreamFieldPanel("about_us_cards"),
    ]