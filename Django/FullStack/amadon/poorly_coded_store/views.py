from django.shortcuts import redirect, render
from .models import Order, Product

def index(request):
    context = {
        "all_products": Product.objects.all()
    }
    return render(request, "store/index.html", context)

def display_checkout(request):
    order_tmp = Order.objects.last()
    total = order_tmp.total_order_items()
    total_quantity = total['total_quantity']
    total_price = total['total_price']
    total_charge = order_tmp.total_price
    context={
        "quantity": total_quantity,
        "total_price": total_price,
        "total_charge": total_charge,
    }

    return render(request, "store/checkout.html", context)

def checkout(request):
    quantity_from_form = int(request.POST["quantity"])
    product = Product.objects.get(id=request.POST['product-id'])
    price_from_form = float(product.price)
    total_charge = quantity_from_form * price_from_form

    print("Charging credit card...")
    Order.objects.create(quantity_ordered=quantity_from_form, total_price=total_charge)

    return redirect('/checkout')