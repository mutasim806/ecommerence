from django.test import TestCase, Client
from product.models import *


class TestModels(TestCase):
    def setUp(self):
        self.categories = Categories.objects.create(
            category_name='Mobile'
        )
        self.product = Product.objects.create(
            product_name='Iphone',
            category=self.categories
        )
        self.ProductDetails = ProductDetails.objects.create(
            price=2100.00,
            color='Black',
            warranty='2years',
            weightAndDimension='1.2',
            display='5 inch',
            chip='ok',
            iSightCamera='yes',
            vedioRecording='yes',
            quantity=4,
            product=self.product
        )
        self.Specifications = Specifications.objects.create(
            specification='4GB RAM',
            product=self.product
        )
        self.Description = Description.objects.create(
            FeatureName='Camera',
            Description='xyz',
            Image='/home/mutasim/Desktop/project/ecommerence/media/Images/iphone-6s.jpg',
            product=self.product
        )
        self.Images = Images.objects.create(
            Images='/home/mutasim/Desktop/project/ecommerence/media/Images/iphone-6s.jpg',
            product=self.product
        )
        self.capacity = Capacity.objects.create(
            Capacity='128GB',
            product=self.product
        )

    def test_categories(self):
        self.assertEquals(self.categories.category_name, 'Mobile')

    def test_Product(self):
        self.assertEquals(self.product.product_name, 'Iphone')
        self.assertEquals(self.product.category.category_name, 'Mobile')
        self.assertEquals(self.product.__str__(), 'Iphone')

    def test_productid(self):
        post = Product.objects.get(id=1)
        self.assertEquals(post.product_name, 'Iphone')

    def test_ProductDetails(self):
        self.assertEquals(self.ProductDetails.price, 2100.00)
        self.assertEquals(self.product.category.category_name, 'Mobile')
        self.assertEquals(self.ProductDetails.__str__(), 'Iphone')

    def test_specification(self):
        self.assertEquals(self.Specifications.__str__(), 'Iphone')

    def test_Description(self):
        self.assertEquals(self.Description.Image, '/home/mutasim/Desktop/project/ecommerence/media/Images/iphone-6s.jpg')
        self.assertEquals(self.Description.__str__(), 'Iphone')

    def test_images(self):
        self.assertEquals(self.Images.Images, '/home/mutasim/Desktop/project/ecommerence/media/Images/iphone-6s.jpg')
        self.assertEquals(self.Images.__str__(), 'Iphone')

    def test_capacity(self):
        self.assertEquals(self.capacity.__str__(), self.capacity.Capacity)


