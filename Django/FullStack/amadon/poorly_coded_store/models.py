from django.db import models

class Product(models.Model):
    description = models.CharField(max_length=45)
    price = models.DecimalField(decimal_places=2, max_digits=5)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Order(models.Model):
    quantity_ordered = models.IntegerField()
    total_price = models.DecimalField(decimal_places=2, max_digits=6)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def total_order_items(self):
        orders = Order.objects.all()
        total_quantity = 0
        total_price = 0

        for order in orders.all():
            total_quantity += order.quantity_ordered
            total_price += order.total_price
        obj = {
            "total_quantity": total_quantity,
            "total_price": total_price
        }
        return obj


    # def total_order_