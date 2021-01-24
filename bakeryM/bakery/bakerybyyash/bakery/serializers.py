from rest_framework import serializers
from .models import Order, BakeryItem, Inventory
from django.contrib.auth.models import User
from bakery import validations


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'email',  'password',
                  )

    def save(self, **kwargs):
        data = self.data
        user = User.objects.create_user(**data)
        if isinstance(user, User):
            return True
        else:
            return False


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('id', 'bakeryitem', 'quantity_ordered', 'payable_amount')

    def save(self, request, **kwargs):
        response = {"error": "Something went wrong"}
        try:
            data = self.data
            quantity_ordered = data.get('quantity_ordered')
            item = BakeryItem.objects.get(pk=data.get('bakeryitem'))
            payable_amount = data.get('payable_amount')
            data.update({
                "bakeryitem": item,
                "user": request.user
            })
            # validate stock
            validation_response, status = validations.validate_stock(**data)
            if not status:
                response.update({"error": validation_response})
                return response, False
            # validate price
            validation_response, status = validations.validate_price(**data)
            if not status:
                response.update({"error": validation_response})
                return response, False

            order = Order.objects.create(**data)
            if isinstance(order, Order):
                updation_response = validations.update_inventory(**data)
                if updation_response:
                    return order, True
                else:
                    raise Exception
            else:
                raise Exception
        except Exception as e:
            return response, False


class BakeryItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = BakeryItem
        fields = ('id', 'name', 'sell_price')
