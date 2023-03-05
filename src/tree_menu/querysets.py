from django.db import models


class MenuItemsQuerySet(models.QuerySet):

    def for_tree_menu(self) -> "MenuItemsQuerySet":
        return self.select_related("menu")
