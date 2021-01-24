from .models import Order, BakeryItem, Inventory


def validate_price(**kwargs):

    quantity_ordered = kwargs.get('quantity_ordered')
    payable_amount = kwargs.get('payable_amount')
    item = kwargs.get('bakeryitem')
    selling_price = item.sell_price * quantity_ordered
    if payable_amount != selling_price:
        response = f"Please pay the full amount of {selling_price}"
        return response, False
    else:
        return None, True


def validate_stock(**kwargs):
    quantity_ordered = kwargs.get('quantity_ordered')
    item = kwargs.get('bakeryitem')
    ingredients_list = item.ingredientsbakeryitemmapping_set.all()
    for ingredient in ingredients_list:
        available_quantity = Inventory.objects.get(
            pk=ingredient.pk).quantity_available
        quantity_per_item = ingredient.quantity_needed
        if available_quantity < (quantity_per_item*quantity_ordered):
            response = "We will not be able to take that order. We are out of stock. Please try lesser quantity"
            return response, False
        else:
            return None, True
    return None, True


def update_inventory(**kwargs):
    try:
        quantity_ordered = kwargs.get('quantity_ordered')
        item = kwargs.get('bakeryitem')
        ingredients_list = item.ingredientsbakeryitemmapping_set.all()
        for ingredient in ingredients_list:
            inv_obj = Inventory.objects.get(pk=ingredient.pk)
            available_quantity = inv_obj.quantity_available
            quantity_per_item = ingredient.quantity_needed
            left_quantity = available_quantity - \
                (quantity_per_item*quantity_ordered)
            inv_obj.quantity_available = left_quantity
            inv_obj.save()
        return True
    except Exception:
        return False
