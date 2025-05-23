"""Functions to keep track and alter inventory."""


def create_inventory(items):
    """Create a dict that tracks the amount (count) of each element on the `items` list.

    :param items: list - list of items to create an inventory from.
    :return: dict - the inventory dictionary.
    """
    inventory = {}
    for value in list(set(items)):
        count = 0
        for item in items:
            if value == item:
                count += 1
        inventory[value] = count
    return inventory

def add_items(inventory, items):
    """Add or increment items in inventory using elements from the items `list`.

    :param inventory: dict - dictionary of existing inventory.
    :param items: list - list of items to update the inventory with.
    :return: dict - the inventory updated with the new items.
    """

    items = create_inventory(items)

    for key, value in items.items():
        if key in inventory:
            inventory[key] += value
        else:
            inventory[key] = value
    return inventory

def decrement_items(inventory, items):
    """Decrement items in inventory using elements from the `items` list.

    :param inventory: dict - inventory dictionary.
    :param items: list - list of items to decrement from the inventory.
    :return: dict - updated inventory with items decremented.
    """
    items = create_inventory(items)

    for key, value in items.items():
        if key in inventory:
            if value > inventory[key]:
                inventory[key] = 0
            else:
                inventory[key] -= value

    return inventory

def remove_item(inventory, item):
    """Remove item from inventory if it matches `item` string.

    :param inventory: dict - inventory dictionary.
    :param item: str - item to remove from the inventory.
    :return: dict - updated inventory with item removed. Current inventory if item does not match.
    """
    if item in inventory:
        inventory.pop(item)
    return inventory

def list_inventory(inventory):
    """Create a list containing only available (item_name, item_count > 0) pairs in inventory.

    :param inventory: dict - an inventory dictionary.
    :return: list of tuples - list of key, value pairs from the inventory dictionary.
    """
    list_inventory_dict = []
    for key, value in inventory.items():
        if value != 0:
            list_inventory_dict.append((key, value))

    return list_inventory_dict

