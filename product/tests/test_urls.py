from django.test import SimpleTestCase
from django.urls import reverse, resolve
from product.views import ShowView, DetailsView


class TestUrls(SimpleTestCase):
    def test_Show_url_is_resolved(self):
        url = reverse('product:show')
        # print(resolve(url))
        self.assertEqual(resolve(url).func.view_class, ShowView)

    def test_Detail_url_is_resolved(self):
        url = reverse('product:details', args=(1,))
        self.assertEqual(resolve(url).func.view_class, DetailsView)

