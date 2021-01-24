from django.contrib import admin
from .models import Ingredient, BakeryItem, IngredientsBakeryItemMapping, Inventory, Order
# Register your models here.


class IngredientsBakeryItemMappingInlineAdmin(admin.TabularInline):
    model = IngredientsBakeryItemMapping
    extra = 0


class InventoryInlineAdmin(admin.TabularInline):
    model = Inventory


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price')
    search_fields = ('id', 'name', 'price')
    list_filter = ('id', 'name', 'price')
    inlines = [InventoryInlineAdmin, ]


@admin.register(BakeryItem)
class BakeryItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'cost_price', 'sell_price')
    search_fields = ('id', 'name', 'cost_price', 'sell_price')
    list_filter = ('id', 'name', 'cost_price', 'sell_price')
    inlines = [IngredientsBakeryItemMappingInlineAdmin, ]


@admin.register(IngredientsBakeryItemMapping)
class IngredientsBakeryItemMappingAdmin(admin.ModelAdmin):
    list_display = ('id', 'bakeryitem', 'ingredient', 'quantity_needed')
    search_fields = ('id', 'bakeryitem', 'ingredient', 'quantity_needed')
    list_filter = ('id', 'bakeryitem', 'ingredient', 'quantity_needed')


@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'ingredient', 'quantity_available')
    search_fields = ('id', 'ingredient', 'quantity_available')
    list_filter = ('id', 'ingredient', 'quantity_available')


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'bakeryitem', 'quantity_ordered', 'payable_amount')
    search_fields = ('id', 'bakeryitem', 'quantity_ordered', 'payable_amount')
    list_filter = ('id', 'bakeryitem', 'quantity_ordered', 'payable_amount')
