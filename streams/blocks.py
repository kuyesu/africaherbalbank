from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ForeignKey
from wagtail.core.models import Page
from wagtail.core import blocks, models
from wagtail.core.blocks.field_block import PageChooserBlock
from wagtail.core.templatetags.wagtailcore_tags import richtext
from wagtail.images.blocks import ImageChooserBlock
from wagtailstreamforms.blocks import WagtailFormBlock
from contact.models import ContactPage

class TitleAndTextBlock(blocks.StructBlock):
    """Title and text and nothing else."""

    title = blocks.CharBlock(required=True, help_text="Add your title")
    text = blocks.TextBlock(required=True, help_text="Add additional text")

    class Meta:  # noqa
        template = "streams/title_and_text_block.html"
        icon = "edit"
        label = "Title & Text"


class CardBlock(blocks.StructBlock):
    """Cards with image and text and button(s)."""

    banner_image_1 = ImageChooserBlock(required=True)
    banner_title_1 = blocks.CharBlock(required=True, help_text="Add your title")
    banner_text_1 = blocks.TextBlock(required=True, max_length=200)
    
    banner_image_2 = ImageChooserBlock(required=True)
    banner_title_2 = blocks.CharBlock(required=True, help_text="Add your title")
    banner_text_2= blocks.TextBlock(required=True, max_length=200)
    
    banner_image_3 = ImageChooserBlock(required=True)
    banner_title_3 = blocks.CharBlock(required=True, help_text="Add your title")
    banner_text_3 = blocks.TextBlock(required=True, max_length=200)
    
    banner_image_4 = ImageChooserBlock(required=True)
    banner_title_4 = blocks.CharBlock(required=True, help_text="Add your title")
    banner_text_4 = blocks.TextBlock(required=True, max_length=200)
    
    banner_image_5 = ImageChooserBlock(required=True)
    banner_title_5 = blocks.CharBlock(required=True, help_text="Add your title")
    banner_text_5 = blocks.TextBlock(required=True, max_length=200)
    


    class Meta:  # noqa
        template = "streams/card/card_staff.html"
        icon = "placeholder"
        label = "Staff Cards"

class Works(blocks.StructBlock):
    title = blocks.CharBlock(required=True, help_text="Add your title")
   
    our_work = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("image", ImageChooserBlock(required=True)),
                ("title", blocks.CharBlock(required=True, max_length=125)),
                ("text", blocks.TextBlock(required=True, max_length=80)),
                ("button_page", blocks.PageChooserBlock(required=False)),
                (
                    "button_url",
                    blocks.URLBlock(
                        required=False,
                        help_text="If the button page above is selected, that will be used first.",  # noqa
                    ),
                ),
            ]
        )
    )
    class Meta:  # noqa
        template = "streams/works.html"
        icon = "placeholder"
        label = "Works"


"""Home page Section Popular herbs"""


class UpConingEvents(blocks.StructBlock):
    title = blocks.CharBlock(required=True, help_text="Add your title")
    brief_description = blocks.TextBlock(required=True, help_text="Add additional text")
    # apply = WagtailFormBlock()
    # application_form = ContactPage()
    upcoming_events = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("image", ImageChooserBlock(required=True)),
                ("title", blocks.CharBlock(required=True, max_length=125)),
                ("text", blocks.TextBlock(required=True)),
                
                
            ]
        )
    )
    class Meta:  # noqa
        template = "streams/events.html"
        icon = "placeholder"
        label = "Events"





class Activities(blocks.StructBlock):
    title = blocks.CharBlock(required=True, help_text="Add your title")
    brief_description = blocks.TextBlock(required=True, help_text="Add additional text")
   
    our_activities = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("image", ImageChooserBlock(required=True)),
                ("title", blocks.CharBlock(required=True, max_length=40)),
                ("text", blocks.TextBlock(required=True, max_length=200)),
                ("button_page", blocks.PageChooserBlock(required=False)),
                (
                    "button_url",
                    blocks.URLBlock(
                        required=False,
                        help_text="If the button page above is selected, that will be used first.",  # noqa
                    ),
                ),
            ]
        )
    )
    class Meta:  # noqa
        template = "streams/activities.html"
        icon = "placeholder"
        label = "Activity"





class SlidingImage(blocks.StructBlock):
    """These are for sliding images"""
    title = blocks.CharBlock(required=True, help_text="Add your title")
    Sliding_Images = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("image", ImageChooserBlock(required=True)),
                
                
            ]
        )
    )

    class Meta: #noqa
        template = "streams/sliding_images.html"
        icon = "image"
        label = "Sliding Image"



       
class JumboBanner(blocks.StructBlock):
    """Jumbo banner for the bottom"""
    title = blocks.CharBlock(required=True, help_text="Add your title")
    JumboBanner_Card = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("title", blocks.CharBlock(required=True)),
                ("subtitle",blocks.TextBlock(required=True, max_length=200)),
                ("image", ImageChooserBlock(required=False)),
                # ("Link_to_a_page", blocks.CharBlock(required=True)),
                ("Link_to_external_page", blocks.CharBlock(required=False)),
                ("button_page", blocks.PageChooserBlock(required=False)),
                (
                    "button_url",
                    blocks.URLBlock(
                        required=False,
                        help_text="If the button page above is selected, that will be used first.",  # noqa
                    ),
                ),
            ]
        )
    )


    class Meta: #noqa
        template = "streams/jumbobanner_page.html"
        icon = "image"
        label = "Large Banner"

class SmallBanner(blocks.StructBlock):
    """Jumbo banner for the bottom"""
    title = blocks.CharBlock(required=True, help_text="Add your title")
    small_banner = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("title", blocks.CharBlock(required=True)),
                ("subtitle",blocks.TextBlock(required=True, max_length=200)),
                ("image", ImageChooserBlock(required=False)),
                # ("Link_to_a_page", blocks.CharBlock(required=False)),
                ("Link_to_external_page", blocks.CharBlock(required=False)),
                ("button_page", blocks.PageChooserBlock(required=False)),
                (
                    "button_url",
                    blocks.URLBlock(
                        required=False,
                        help_text="If the button page above is selected, that will be used first.",  # noqa
                    ),
                ),
            ]
        )
    )


    class Meta: #noqa
        template = "streams/small_banner.html"
        icon = "image"
        label = "Small Banner"



class CardMessage(blocks.StructBlock):
    title = blocks.CharBlock(required=True, help_text="Add your title")

    message_Card = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("title", blocks.CharBlock(required=True, max_length=40)),
                ("text", blocks.TextBlock(required=True, max_length=200)),
                ("image", ImageChooserBlock(required=True)),
                ("button_page", blocks.PageChooserBlock(required=False)),
                (
                    "button_url",
                    blocks.URLBlock(
                        required=False,
                        help_text="If the button page above is selected, that will be used first.",  # noqa
                    ),
                ),
            ]
        )
    )
    class Meta: # noqa
        template = "streams/card/contact/message.html"
        icon = "edit"
        label = "Message Card"
        
class CardLapping(blocks.StructBlock):
    title = blocks.CharBlock(required=True, help_text="Add your title")

    Lapping_card = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("title", blocks.CharBlock(required=True, max_length=40)),
                ("subtitle", blocks.TextBlock(required=True, max_length=200)),
                ("text", blocks.TextBlock(required=True, max_length=200)),
                ("image", ImageChooserBlock(required=False)),
                ("button_page", blocks.PageChooserBlock(required=False)),
                (
                    "button_url",
                    blocks.URLBlock(
                        required=False,
                        help_text="If the button page above is selected, that will be used first.",  # noqa
                    ),
                ),
            ]
        )
    )
    class Meta: # noqa
        template = "streams/card/lapping_card.html"
        icon = "edit"
        label = "Lapping Card"
        
class CardLight(blocks.StructBlock):
    title = blocks.CharBlock(required=True, help_text="Add your title")

    Light_Card = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("title", blocks.CharBlock(required=True, max_length=40)),
                ("text", blocks.TextBlock(required=True, max_length=200)),
                ("image", ImageChooserBlock(required=True)),
                ("button_page", blocks.PageChooserBlock(required=False)),
                (
                    "button_url",
                    blocks.URLBlock(
                        required=False,
                        help_text="If the button page above is selected, that will be used first.",  # noqa
                    ),
                ),
            ]
        )
    )
    class Meta: # noqa
        template = "streams/card/light_card.html"
        icon = "edit"
        label = "Contact Light Card"

class CardLightSmall(blocks.StructBlock):
    title = blocks.CharBlock(required=True, help_text="Add your title")

    Small_card = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("title", blocks.CharBlock(required=True, max_length=40)),
                ("text", blocks.TextBlock(required=True, max_length=200)),
                ("image", ImageChooserBlock(required=True)),
                ("button_page", blocks.PageChooserBlock(required=False)),
                (
                    "button_url",
                    blocks.URLBlock(
                        required=False,
                        help_text="If the button page above is selected, that will be used first.",  # noqa
                    ),
                ),
            ]
        )
    )
    class Meta: # noqa
        template = "streams/card/smallcard.html"
        icon = "edit"
        label = "Small Contact Light Card"


class CardWave(blocks.StructBlock):

    Wave_card = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("title", blocks.CharBlock(required=True, max_length=40)),
                ("text", blocks.TextBlock(required=True, max_length=200)),
                ("image", ImageChooserBlock(required=True)),
                ("button_page", blocks.PageChooserBlock(required=False)),
                (
                    "button_url",
                    blocks.URLBlock(
                        required=False,
                        help_text="If the button page above is selected, that will be used first.",  # noqa
                    ),
                ),
            ]
        )
    )
    class Meta: # noqa
        template = "streams/card/card_wave.html"
        icon = "edit"
        label = "Wave Card"
        max_count=4


class CardContact(blocks.StructBlock):
    title = blocks.CharBlock(required=True, help_text="Add your title")

    Contact_card = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("title", blocks.CharBlock(required=True, max_length=40)),
                ("text", blocks.TextBlock(required=True, max_length=200)),
                ("image", ImageChooserBlock(required=True)),
                ("button_page", blocks.PageChooserBlock(required=False)),
                (
                    "button_url",
                    blocks.URLBlock(
                        required=False,
                        help_text="If the button page above is selected, that will be used first.",  # noqa
                    ),
                ),
            ]
        )
    )
    class Meta: # noqa
        template = "streams/card/contact/contact.html"
        icon = "contact"
        label = "Contact Card"
        
class CardSubscribe(blocks.StructBlock):
    title = blocks.CharBlock(required=True, help_text="Add your title")

    Subscribe_Card = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("title", blocks.CharBlock(required=True, max_length=40)),
                ("text", blocks.TextBlock(required=True, max_length=200)),
                ("image", ImageChooserBlock(required=True)),
                ("button_page", blocks.PageChooserBlock(required=False)),
                (
                    "button_url",
                    blocks.URLBlock(
                        required=False,
                        help_text="If the button page above is selected, that will be used first.",  # noqa
                    ),
                ),
            ]
        )
    )
    class Meta: # noqa
        template = "streams/card/contact/subscribe.html"
        icon = "edit"
        label = "Subscribe Card"
        
class CardCode(blocks.StructBlock):
    title = blocks.CharBlock(required=True, help_text="Add your title")

    Code_card = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("title", blocks.CharBlock(required=True, max_length=140)),
                ("text", blocks.TextBlock(required=True, max_length=200)),
                ("image", ImageChooserBlock(required=True)),
                ("button_page", blocks.PageChooserBlock(required=False)),
                (
                    "button_url",
                    blocks.URLBlock(
                        required=False,
                        help_text="If the button page above is selected, that will be used first.",  # noqa
                    ),
                ),
            ]
        )
    )
    class Meta: # noqa
        template = "streams/card/code.html"
        icon = "code"
        label = "Code Card"

class CardImage(blocks.StructBlock):
    title = blocks.CharBlock(required=True, help_text="Add your title")

    Image_Card = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("title", blocks.CharBlock(required=True, max_length=140)),
                ("text", blocks.TextBlock(required=True, max_length=200)),
                ("banner_image", ImageChooserBlock(required=True)),
                ("fancy_herb_image", blocks.ListBlock(
                    blocks.StructBlock(
                         [
                        ("image", ImageChooserBlock(required=True))
                    ],
                    required=True,
                    )
                   
                )),
                ("button_page", blocks.PageChooserBlock(required=False)),
                (
                    "button_url",
                    blocks.URLBlock(
                        required=False,
                        help_text="If the button page above is selected, that will be used first.",  # noqa
                    ),
                ),
            ]
        )
    )
    class Meta: # noqa
        template = "streams/card/image_card.html"
        icon = "image"
        label = "Card with Image Card"

class CardTeam(blocks.StructBlock):
    title = blocks.CharBlock(required=True, help_text="Add your title")
    subtitle = blocks.CharBlock(required=True, help_text="Add your title")
    Team_Card = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("Role", blocks.CharBlock(required=True, max_length=40)),
                ("Name", blocks.TextBlock(required=True, max_length=200)),
                ("twitter", blocks.TextBlock(required=True, max_length=200)),
                ("whatsapp", blocks.TextBlock(required=True, max_length=200)),
                ("facebook", blocks.TextBlock(required=True, max_length=200)),
                ("statement", blocks.TextBlock(required=True, max_length=200)),
                ("image", ImageChooserBlock(required=True)),
                ("button_page", blocks.PageChooserBlock(required=False)),
                (
                    "button_url",
                    blocks.URLBlock(
                        required=False,
                        help_text="If the button page above is selected, that will be used first.",  # noqa
                    ),
                ),
            ]
        )
    )
    class Meta: # noqa
        template = "streams/card/team_card.html"
        icon = "image"
        label = "Team Card"


class CardGeneric(blocks.StructBlock):
    title = blocks.CharBlock(required=True, help_text="Add your title")
    subtitle = blocks.CharBlock(required=True, help_text="Add your title")

    Generic_Card = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("title", blocks.CharBlock(required=True, max_length=140)),
                ("text", blocks.TextBlock(required=True, max_length=200)),
                ("image", ImageChooserBlock(required=True)),
                ("button_page", blocks.PageChooserBlock(required=False)),
                (
                    "button_url",
                    blocks.URLBlock(
                        required=False,
                        help_text="If the button page above is selected, that will be used first.",  # noqa
                    ),
                ),
            ]
        )
    )
    class Meta: # noqa
        template = "streams/card/generic_card.html"
        icon = "doc-full"
        label = "Generic Card" 

class CardActivity(blocks.StructBlock):
    title = blocks.CharBlock(required=True, help_text="Add your title")

    Activities_card = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("project", blocks.CharBlock(required=True, max_length=140)),
                ("text", blocks.TextBlock(required=True, max_length=200)),
                ("stats", blocks.IntegerBlock(required=True)), 
                ("button_page", blocks.PageChooserBlock(required=False)),
                
            ]
        )
    )
    class Meta: # noqa
        template = "streams/card/activity_card.html"
        icon = "doc-full"
        label = "Our Srvices"

class CardTestimonies(blocks.StructBlock):
    title = blocks.CharBlock(required=True, help_text="Add your title")

    Testimonies_card = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("title", blocks.CharBlock(required=True, max_length=140)),
                ("subtitle", blocks.CharBlock(required=True, max_length=240)),
                
                ("image", ImageChooserBlock(required=True)),
                ("Name", blocks.CharBlock(required=True, max_length=40)),
                ("job_title", blocks.CharBlock(required=True, max_length=40)),
                ("text", blocks.TextBlock(required=False, max_length=200)),
                ("rating", blocks.IntegerBlock()),
                ("button_page", blocks.PageChooserBlock(required=False)),
                (
                    "button_url",
                    blocks.URLBlock(
                        required=False,
                        help_text="If the button page above is selected, that will be used first.",  # noqa
                    ),
                ),
            ]
        )
    )
    class Meta: # noqa
        template = "streams/card/testimonies_card.html"
        icon = "phone"
        label = "Testimonies Card"

class CardTable(blocks.StructBlock):
    title = blocks.CharBlock(required=True, help_text="Add your title")

    Table_Card = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("title", blocks.CharBlock(required=True, max_length=140)),
                ("subtitle", blocks.CharBlock(required=True, max_length=240)),
                
                ("image", ImageChooserBlock(required=True)),
                ("Name", blocks.CharBlock(required=True, max_length=40)),
                ("job_title", blocks.CharBlock(required=True, max_length=40)),
                ("text", blocks.TextBlock(required=False, max_length=200)),
                ("button_page", blocks.PageChooserBlock(required=False)),
                (
                    "button_url",
                    blocks.URLBlock(
                        required=False,
                        help_text="If the button page above is selected, that will be used first.",  # noqa
                    ),
                ),
            ]
        )
    )
    class Meta: # noqa
        template = "streams/table_card.html"
        icon = "table"
        label = "Table Card"
 
class Technologies(blocks.StructBlock):
    title = blocks.CharBlock(required=True, help_text="Add your title")

    Technologies = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("title", blocks.CharBlock(required=True, max_length=140)),
                ("text", blocks.TextBlock(required=False, max_length=200)),
                ("image", ImageChooserBlock(required=True)),
                ("button_page", blocks.PageChooserBlock(required=False)),
                (
                    "button_url",
                    blocks.URLBlock(
                        required=False,
                        help_text="If the button page above is selected, that will be used first.",  # noqa
                    ),
                ),
            ]
        )
    )
    class Meta: # noqa
        template = "streams/technology.html"
        icon = "phone"
        label = "Technology"
        
class Testimonies(blocks.StructBlock):
    title = blocks.CharBlock(required=True, max_legngth=80, help_text="Add your title")
    subtitle = blocks.TextBlock(required=True, max_legngth=100, help_text="Add your subtitle")

    Testimonies_FrOm_user = blocks.ListBlock(
        blocks.StructBlock(
            [
                
                ("image", ImageChooserBlock(required=True)),
                ("Name", blocks.CharBlock(required=True, max_length=40)),
                ("job_title", blocks.CharBlock(required=True, max_length=40)),
                ("text", blocks.TextBlock(required=False, max_length=200)),
                ("button_page", blocks.PageChooserBlock(required=False)),
                (
                    "button_url",
                    blocks.URLBlock(
                        required=False,
                        help_text="If the button page above is selected, that will be used first.",  # noqa
                    ),
                ),
            ]
        )
    )
    class Meta: # noqa
        template = "streams/testimonies.html"
        icon = "phone"
        label = "Testimonies"  
        
class Partners(blocks.StructBlock):
    title = blocks.CharBlock(required=True, help_text="Add your title")

    patners = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("title", blocks.CharBlock(required=True, max_length=140)),
                ("image", ImageChooserBlock(required=True)),
                ("button_page", blocks.PageChooserBlock(required=False)),
                (
                    "button_url",
                    blocks.URLBlock(
                        required=False,
                        help_text="If the button page above is selected, that will be used first.",  # noqa
                    ),
                ),
            ]
        )
    )
    class Meta: # noqa
        template = "streams/partners.html"
        icon = "phone"
        label = "Partners"
        
class ClassicCard(blocks.StructBlock):
    title = blocks.CharBlock(required=True, help_text="Add your title")

    classic_content = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("title", blocks.CharBlock(required=True, max_length=100)),
                ("subtitle", blocks.TextBlock(required=True, max_length=200)),
                ("image", ImageChooserBlock(required=True)),
                ("button_page", blocks.PageChooserBlock(required=False)),
                (
                    "button_url",
                    blocks.URLBlock(
                        required=False,
                        help_text="If the button page above is selected, that will be used first.",  # noqa
                    ),
                ),
            ]
        )
    )
    class Meta: # noqa
        template = "streams/card/classic_card.html"
        icon = "card"
        label = "Classic Card"
        

class FaqCard(blocks.StructBlock):
    category = blocks.CharBlock(required=True, help_text="Add your title")

    questions_and_answer = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("question", blocks.CharBlock(required=True, max_length=100)),
                ("paragraph", blocks.TextBlock(required=True, max_length=1000)),
                
            ]
        )
    )
    class Meta: # noqa
        template = "streams/faq_card.html"
        icon = "card"
        label = "FAQ"  
        

class FormCard(blocks.StructBlock):
    heading = blocks.CharBlock(required=True, help_text="Add your title")

    body = blocks.ListBlock(
        blocks.StructBlock(
            [
                ('paragraph', blocks.RichTextBlock()),
                ('form', WagtailFormBlock()),
            ]
        )
    )
    class Meta: # noqa
        template = "streams/form/form_card.html"
        icon = "form"
        label = "Form"  
        






# -------------------------------------------------------------------------------------
class BannerTransparent(blocks.StructBlock):

    banner_content = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("banner_title", blocks.CharBlock(required=True, max_length=100)),
                ("banner_subtitle", blocks.TextBlock(required=True, max_length=200)),
                ("banner_image", ImageChooserBlock(required=True)),
                ("button_page", blocks.PageChooserBlock(required=False)),
                (
                    "button_url",
                    blocks.URLBlock(
                        required=False,
                        help_text="If the button page above is selected, that will be used first.",  # noqa
                    ),
                ),
            ]
        )
    )
    class Meta: # noqa
        template = "streams/banner/banner_transparent.html"
        icon = "card"
        label = "Transparent Banner"
        
        

class Banner(blocks.StructBlock):

    banner_content = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("banner_title", blocks.CharBlock(required=True, max_length=100)),
                ("banner_subtitle", blocks.TextBlock(required=True, max_length=200)),
                ("banner_image", ImageChooserBlock(required=True)),
                ("button_page", blocks.PageChooserBlock(required=False)),
                (
                    "button_url",
                    blocks.URLBlock(
                        required=False,
                        help_text="If the button page above is selected, that will be used first.",  # noqa
                    ),
                ),
            ]
        )
    )
    class Meta: # noqa
        template = "streams/banner/banner.html"
        icon = "card"
        label = "curve Banner"
        

class BannerOpacity(blocks.StructBlock):

    banner_content = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("banner_title", blocks.CharBlock(required=True, max_length=100)),
                ("banner_subtitle", blocks.TextBlock(required=True, max_length=200)),
                ("banner_image", ImageChooserBlock(required=True)),
                ("button_page", blocks.PageChooserBlock(required=False)),
                (
                    "button_url",
                    blocks.URLBlock(
                        required=False,
                        help_text="If the button page above is selected, that will be used first.",  # noqa
                    ),
                ),
            ]
        )
    )
    class Meta: # noqa
        template = "streams/banner/opacity.html"
        icon = "card"
        label = "Opacity Banner"


class BannerCurveOpacity(blocks.StructBlock):

    banner_content = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("banner_title", blocks.CharBlock(required=True, max_length=100)),
                ("banner_subtitle", blocks.TextBlock(required=True, max_length=200)),
                ("banner_image", ImageChooserBlock(required=True)),
                ("button_page", blocks.PageChooserBlock(required=False)),
                (
                    "button_url",
                    blocks.URLBlock(
                        required=False,
                        help_text="If the button page above is selected, that will be used first.",  # noqa
                    ),
                ),
            ]
        )
    )
    class Meta: # noqa
        template = "streams/banner/curve_opacity.html"
        icon = "card"
        label = "Opacity Curve Banner"
# ------------------------------------------------------------------------




class RichtextBlock(blocks.StructBlock):
    """Richtext with all the features."""
    comment = blocks.RichTextBlock(required=True, help_text="Add your title")
    class Meta:  # noqa
        template = "streams/richtext_block_copy.html"
        icon = "doc-full"
        label = "Full RichText"


class SimpleRichtextBlock(blocks.StructBlock):
    comment = blocks.TextBlock(required=True, help_text="Add your title")

    class Meta:  # noqa
        template = "streams/richtext_block.html"
        icon = "comment"
        label = "Comment"


class CTABlock(blocks.StructBlock):
    """A simple call to action section."""

    title = blocks.CharBlock(required=True, max_length=60)
    text = blocks.RichTextBlock(required=True, features=["bold", "italic"])
    button_page = blocks.PageChooserBlock(required=False)
    button_url = blocks.URLBlock(required=False)
    button_text = blocks.CharBlock(required=True, default='Learn More', max_length=40)
    

    class Meta:  # noqa
        template = "streams/cta_block.html"
        icon = "placeholder"
        label = "Call to Action"


class LinkStructValue(blocks.StructValue):
    """Additional logic for our urls."""

    def url(self):
        button_page = self.get('button_page')
        button_url = self.get('button_url')
        if button_page:
            return button_page.url
        elif button_url:
            return button_url

        return None

    # def latest_posts(self):
    #     return BlogDetailPage.objects.live()[:3]


class ButtonBlock(blocks.StructBlock):
    """An external or internal URL."""
    button_name = blocks.CharBlock(required=True)
    button_dark = blocks.PageChooserBlock(required=False, help_text='If selected, this url will be used first')
    button_colored = blocks.PageChooserBlock(required=False, help_text='If selected, this url will be used first')
    button_transparent = blocks.PageChooserBlock(required=False, help_text='If selected, this url will be used first')
    button_search = blocks.PageChooserBlock(required=False, help_text='If selected, this url will be used first')
    button_medium = blocks.PageChooserBlock(required=False, help_text='If selected, this url will be used first')
    button_small = blocks.PageChooserBlock(required=False, help_text='If selected, this url will be used first')
    button_url = blocks.URLBlock(required=False, help_text='If added, this url will be used secondarily to the button page')

    # def get_context(self, request, *args, **kwargs):
    #     context = super().get_context(request, *args, **kwargs)
    #     context['latest_posts'] = BlogDetailPage.objects.live().public()[:3]
    #     return context

    class Meta:  # noqa
        template = "streams/button_block.html"
        icon = "link"
        label = "Button"
value_class = LinkStructValue     
# ------------------------------------------------------------------------




