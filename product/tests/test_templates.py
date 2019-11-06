from django.http import HttpRequest
from django.template.loader import render_to_string
from django.test import TestCase, Client
from django.urls import reverse
from product.models import *

class TemplateTags(TestCase):
    def test_templatetags(self):
        self.client = Client()
        url = reverse('product:show')
        responce = self.client.get(url)
        self.assertEquals(responce.status_code, 200)
        self.assertTemplateUsed(responce, 'index.html')
        self.assertContains(responce, '<div class="item active"', 1)

    def test_templateviewcontext(self):
        self.c = Client()
        url = reverse('product:show')
        responce = self.c.get(url)
        self.assertSetEqual(responce.context['categories'], Categories.objects.all())
        self.assertCountEqual(responce.context['categories'], Categories.objects.all())
        self.assertTemplateUsed(responce, 'index.html')
        self.assertContains(responce, '<div class="subscription-form">', count=1)
        self.assertContains(responce, '<div class="subscription-form">', status_code=200)
