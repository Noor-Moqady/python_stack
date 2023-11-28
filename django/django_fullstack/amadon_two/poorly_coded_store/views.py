from django.shortcuts import render, redirect
from .models import Order, Product

def index(request):
    # request.session['allamount'] =0
    context = {
        "all_products": Product.objects.all()
    }
    return render(request, "index.html", context)

def checkout(request, id):
    if request.method == 'GET':
        specific_product = Product.objects.get(id=id)
        all_orders = Order.objects.all()
        total_amount_charged = sum(order.total_price for order in all_orders)
        total_amount_quantitiy = sum(order.quantity_ordered for order in all_orders)
        context={
        'specific_product': Product.objects.get(id=id),
        'allorders': Order.objects.all(),
        'total_amount_charged': total_amount_charged,
        'total_amount_quantitiy': total_amount_quantitiy,
        }
        
        return render(request,"checkout.html", context)
    if request.method == 'POST':
        specific_product= Product.objects.get(id=id)
        quantity_from_form = int(request.POST["quantity"])
        price_from_form = float(specific_product.price)
        total_charge = (quantity_from_form) * (price_from_form)

        print("Charging credit card...")
        specific_order=Order.objects.create(quantity_ordered=quantity_from_form, total_price=total_charge)

        # request.session['allamount']+=total_charge
        request.session['specific_order_quantity']=specific_order.quantity_ordered
        request.session['specific_order_total_price']=specific_order.total_price
        
        return redirect('/checkout/'+str(id))
    

def delete(request):
    allorders=Order.objects.all()
    for order in allorders:
        order.delete()
    return redirect("/")