from django.db import models
from django import forms
# from django_countries.countries import COUNTRIES
from django_countries.fields import CountryField

from wagtail.admin.edit_handlers import (
    FieldPanel,
    MultiFieldPanel,
    FieldRowPanel
)
# Create your models here.
class Teams(models.Model):
    
    first_name = models.CharField(max_length=50, blank=False, null=True)
    last_name = models.CharField(max_length=50, blank=False, null=True)
    middle_name  = models.CharField(max_length=50, blank=False, null=True)
    address = models.CharField(max_length=50, blank=False, null=True)
    Country = CountryField()
    
    def __str__(self) -> str:
        return self.first_name
    panels = [
        MultiFieldPanel(
            [
                FieldRowPanel(
                    [
                        FieldPanel("first_name", classname='col6'),
                        FieldPanel("last_name", classname='col6'),
                        FieldPanel("middle_name", classname='col6'),
                    ]
                ),
                FieldPanel("address"),
                FieldPanel("Country"),
            ],
            heading = "Personal Info"
        )
    ]
    class Meta:
        # db_table = ''
        managed = True
        verbose_name = 'Team'
        verbose_name_plural = 'Teams'