from django.shortcuts import render
from django.views import View
from eshop.models import Customer,Order,Product
from datetime import date, timedelta

# Create your views here.
class OrderedProducts(View):
    def get(self, request, customer_id):
        last_days = int(request.GET.get('last_days'))
        filter_date = date.today() - timedelta(days=last_days)

        customer = Customer.objects.filter(pk=customer_id).first()
        orders = Order.objects.filter(customer_id=customer_id,created_at__gt=filter_date).order_by('-created_at')

        products_set = set()
        products = []
        for order in orders:
            if order.product.exists():
                for p in order.product.all():
                    if p.pk in products_set:
                        continue
                    products.append((p.pk, p.name, order.created_at))
                    products_set.add(p.pk)

        context = {"customer": customer, "products": products, "last_days": last_days}

        return render(request, "eshop/customer_orders.html", context)
