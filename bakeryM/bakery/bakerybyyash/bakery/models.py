from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class BaseModel(models.Model):

    name = models.CharField(max_length=64, blank=True, null=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name_plural = 'Base Models'


class Ingredient(BaseModel):

    price = models.FloatField(max_length=64, blank=True, null=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name_plural = 'Ingredients'


class BakeryItem(BaseModel):

    cost_price = models.FloatField(max_length=64, blank=True, null=True)
    sell_price = models.FloatField(max_length=64, blank=True, null=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name_plural = 'Bakery Items'


class IngredientsBakeryItemMapping(models.Model):

    bakeryitem = models.ForeignKey(BakeryItem, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity_needed = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f'{self.bakeryitem} - {self.ingredient}'

    class Meta:
        verbose_name_plural = 'Ingredient Bakery Item Mappings'


class Inventory(models.Model):

    ingredient = models.OneToOneField(Ingredient, on_delete=models.CASCADE)
    quantity_available = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f'{self.ingredient} - {self.quantity_available}'

    class Meta:
        verbose_name_plural = 'Inventory'


class Order(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bakeryitem = models.ForeignKey(BakeryItem, on_delete=models.CASCADE)
    quantity_ordered = models.IntegerField(blank=True, null=True)
    payable_amount = models.FloatField(max_length=64, blank=True, null=True)

    def __str__(self):
        return f'{self.user} ordered {self.quantity_ordered} {self.bakeryitem} for {self.payable_amount}'

    class Meta:
        verbose_name_plural = 'Orders'
