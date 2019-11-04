from decimal import Decimal
from django.conf import settings
from product.models import ProductDetails, Product


class Cart(object):
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, product, quantity=1, update_quantity=False):
        product_id = str(product.id)
        if product_id in self.cart:
            # self.cart[product_id] = {'quantity': 0, 'price': str(ProductDetails.price)}
            product = ProductDetails.objects.get(product_id=product_id)
            self.cart[product_id] = {'product': product}
        # if update_quantity:
        #     self.cart[product_id]['quantity'] = quantity
        # else:
        #     self.cart[product_id]['quantity'] += quantity
        self.save()

    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True

    def remove(self, product):
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def __iter__(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        for product in products:
            self.cart[str(product.id)]['product'] = product

        for item in self.cart.values():
            item['price'] = Decimal(item['price'])
            # item['total_price'] = item['price'] * item['quantity']
            yield item

    # def __len__(self):
    #     return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        total = 0
        for item in self.cart.values():
            total += Decimal(item['price'])
        return total

    def clear(self):
        self.session[settings.CART_SESSION_ID] = {}
        self.session.modified = True