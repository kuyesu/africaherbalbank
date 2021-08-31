from wagtail.contrib.modeladmin.options import (
    ModelAdmin,
    modeladmin_register,
)

from .models import Subscribers
# Register your models here.

class SubscriberAdmin(ModelAdmin):
    model = Subscribers
    menu_label = "Subscribers"
    menu_icon = "placeholder"
    menu_order = 290
    add_to_settings_menu = False
    exlude_from_explorer = False
    list_display = ("email", "fullname")
    search_fields = ("email", "fullname")
    
    
modeladmin_register(SubscriberAdmin)