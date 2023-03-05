from django.contrib import admin

from tree_menu.models import Item
from tree_menu.models import Menu


@admin.register(Item)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ("title", "parent")
    list_filter = ("menu",)
    fieldsets = (("Add new item", {"fields": (("menu", "parent"), "title", "slug")}),)


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ("title", "slug")
