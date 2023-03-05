from django import template

from tree_menu.models import Item

register = template.Library()


@register.inclusion_tag("nested_menu.html", takes_context=True)
def draw_menu(context, menu_name):
    try:
        items = Item.objects.select_related("menu").filter(menu__title=menu_name)
        items_values = items.values()
        items_listed = (list(items_values))
        primary_items = [item for item in items_listed if item.get("parent_id") is None]
        selected_item_id = int(context["request"].GET[menu_name])
        items_id_dict = {item["id"]: item for item in items_listed}
        selected_item_id_list = get_selected_item_id_list(items_id_dict, primary_items, selected_item_id)

        for item in primary_items:
            if item["id"] in selected_item_id_list:
                item["child_items"] = get_child_items(items_values, item["id"], selected_item_id_list)
        result_dict = {"items": primary_items}

    except:
        filtered_items = Item.objects.select_related("menu").filter(menu__title=menu_name, parent=None)
        result_dict = {"items": [item for item in filtered_items.values()]}

    result_dict["menu"] = menu_name
    result_dict["other_querystring"] = get_querystring(context, menu_name)
    return result_dict


def get_querystring(context, menu):
    querystring_args = []
    for key in context["request"].GET:
        if key != menu:
            querystring_args.append(key + "=" + context["request"].GET[key])
    querystring = ("&").join(querystring_args)
    return querystring


def get_child_items(items_values, current_item_id, selected_item_id_list):
    item_list = [item for item in items_values if item.get("parent_id") == current_item_id]
    for item in item_list:
        if item["id"] in selected_item_id_list:
            item["child_items"] = get_child_items(items_values, item["id"], selected_item_id_list)
    return item_list


def get_selected_item_id_list(items_id_dict, primary_item, selected_item_id):
    selected_item_id_list = []
    parent_id = items_id_dict[selected_item_id]["id"]

    while parent_id:
        selected_item_id_list.append(parent_id)
        parent_id = items_id_dict[parent_id].get("parent_id")
    if not selected_item_id_list:
        for item in primary_item:
            if item["id"] == selected_item_id:
                selected_item_id_list.append(selected_item_id)
    return selected_item_id_list
