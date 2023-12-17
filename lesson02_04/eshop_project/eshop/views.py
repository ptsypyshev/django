import uuid
from django.shortcuts import render,redirect
from django.views import View
from eshop.models import Customer,Order,Product
from datetime import date, timedelta
from django.core.files.storage import FileSystemStorage
from .forms import ProductFormWidget

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


class CreateProduct(View):
    def get(self, request):
        form = ProductFormWidget()
        return render(request, 'eshop/create_product.html', {'form': form})
    
    def post(self, request):
        form = ProductFormWidget(request.POST, request.FILES)
        if form.is_valid():
            img = form.cleaned_data['img']
            image_name = CreateProduct.save_img(img)
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            price = form.cleaned_data['price']
            qty = form.cleaned_data['qty']
            
            product = Product(name=name, description=description, price=price, qty=qty, img=image_name)
            product.save()
            return redirect(f'/product/{product.pk}')
        
        return render(request, 'eshop/create_product.html', {'form': form})
    
    @staticmethod
    def save_img(image):
        name = '.'.join((str(uuid.uuid4()), image.name.split('.')[-1]))
        fs = FileSystemStorage()
        fs.save(name, image)
        return name

class ReadProduct(View):
    def get(self, request, product_id):
        product = Product.objects.filter(pk=product_id).first()
        context = {"product": product, "product_id": product_id}
        return render(request, "eshop/read_product.html", context, status=200 if product else 404)
