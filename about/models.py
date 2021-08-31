from django.db import models

# Create your models here.
from django.db import models
from wagtail.core.models import Page

# Create your models here.
class AboutPage(Page):

    template = "about/about_page.html"
    subpage_types = []
    parent_page_types = ['home.HomePage']