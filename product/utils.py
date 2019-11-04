from product.models import *


def get_ecommerence_context_data():
    categories = Categories.objects.all()
    product = Product.objects.all()
    productDetails = ProductDetails.objects.all()
    specification = Specifications.objects.all()
    description = Description.objects.all()
    images = Images.objects.all()
    capacity = Capacity.objects.all()
    product_filter = Product.objects.filter(category_id=1)
    context = {
        'categories': categories,
        'product': product,
        'productDetails': productDetails,
        'specification': specification,
        'description': description,
        'images': images,
        'capacity': capacity,
        'product_filter': product_filter
    }
    return context