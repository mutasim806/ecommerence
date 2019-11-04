from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from product.models import *
import json


class TestView(TestCase):
    def setUp(self):
        self.client = Client()
        self.username = 'admin'
        self.password = 'admin'
        user = User(username=self.username, password=self.password)
        user.save()
        self.client.force_login(user)
        self.show_url = reverse('product:show')
        self.detail_url = reverse('product:details', args=(1,))
        self.category = Categories.objects.create(
            category_name='Mobile'
        )
        self.product = Product.objects.create(
            product_name='huawei',
            category=self.category
        )
        ProductDetails.objects.create(
            price=2300,
            color='Black',
            warranty='2Years',
            weightAndDimension='2.5',
            display='5',
            chip='233',
            iSightCamera='yes',
            vedioRecording='yes',
            quantity=4,
            product=self.product
        )


    def test_showView(self):
        responce = self.client.get(self.show_url)
        self.assertEquals(responce.status_code, 200)
        self.assertTemplateUsed(responce, template_name='index.html')

    def test_DetailView(self):
        responce = self.client.get(self.detail_url)
        self.assertEquals(responce.status_code, 200)
        self.assertTemplateUsed(responce, template_name='product_details.html')

    # def test_DetailView_delete(self):
    #     responce = self.client.delete(self.detail_url, json.dumps({
    #         'id': 1
    #     }))
    #     self.assertEquals(responce.status_code, 204)
    #     self.assertEquals(self.product.product_name.count(), 0)
