from django.shortcuts import render , get_object_or_404
from django.core.paginator import Page, EmptyPage, PageNotAnInteger, Paginator
from django.views import View
from .models import Category, Product
from cart.forms import CartAddProductForm
from baseapp.models import Application
# Create your views here.
class Product_list(View):


    def get(self, request, category_slug=None):

        category = None
        categories = Category.objects.all()
        products = Product.objects.filter(available=True)
        
        # product for in one page
        paginator = Paginator(products, 8)
        page = request.GET.get('page')
        # PAGINATION
        try:
            products = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer deliver the first page
            products = paginator.page(1)
        except EmptyPage:
            # If page is out of range deliver last page of result
            products = paginator.page(paginator.num_pages)
        ##
        applications = Application.objects.all()
        if category_slug:
            category = get_object_or_404(Category, slug=category_slug)
            products = products.filter(category=category)
        return render(request, 'shop/product/list.html', {'category': category,
                                                          'categories': categories,
                                                          'products': products,
                                                          'applications': applications})

    def post(self, request):
        pass

class Product_detail(View):

    def get(self, request, id, slug):
        product = get_object_or_404(Product, id=id, slug=slug, available=True)
        applications = Application.objects.all()
        cart_product_form = CartAddProductForm()
        return render(request, 'shop/product/detail.html', {'product': product,
                                                            'cart_product_form': cart_product_form,
                                                            'applications': applications})
