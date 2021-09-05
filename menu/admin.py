from django.contrib import admin

# Register your models here.
from .models import MenuItem, Menu
from django.contrib import admin
from modeltranslation.admin import TranslationAdmin, TranslationTabularInline
from .models import  MenuItem, Menu
from django.contrib import admin
from modeltranslation.admin import TranslationAdmin, TranslationTabularInline




# class MenuItemInline(TranslationTabularInline):
#     model = MenuItem


# class MenuAdmin(TranslationAdmin):
#     model = Menu
#     inlines = [MenuItemInline,]


# admin.site.register(Menu, MenuAdmin)



# class ThemeAdmin(TranslationAdmin):
#     model = Theme


class MenuItemInline(TranslationTabularInline):
    model = MenuItem


class MenuAdmin(TranslationAdmin):
    model = Menu
    inlines = [MenuItemInline,]


# class CustomCommentAdmin(XtdCommentsAdmin):
#     list_display = ('cid', 'name', 'page', 'object_pk',
#                     'ip_address', 'submit_date', 'followup', 'is_public',
#                     'is_removed')
#     fieldsets = (
#         (None, {'fields': ('content_type', 'page', 'object_pk', 'site')}),
#         ('Content', {'fields': ('user', 'user_name', 'user_email',
#                                 'user_url', 'comment', 'followup')}),
#         ('Metadata', {'fields': ('submit_date', 'ip_address',
#                                  'is_public', 'is_removed')}),
#     )


# admin.site.register(Theme, ThemeAdmin)
admin.site.register(Menu, MenuAdmin)
# admin.site.register(CustomComment, CustomCommentAdmin)
