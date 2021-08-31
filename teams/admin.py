from django.contrib import admin
from django.db import models
from wagtail.contrib.modeladmin.options import (
    ModelAdmin,
    modeladmin_register,
)
from .models import Teams
# Register your models here.

class TeamAdmin(ModelAdmin):
    model = Teams
    menu_label = "Teams"
    menu_icon = "placeholder"
    menu_order = 290
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ("first_name", "last_name", "middle_name", "address", "Country")
    search_fields = ("first_name", "last_name", "middle_name", "address", "Country")

    
    
modeladmin_register(TeamAdmin)
    