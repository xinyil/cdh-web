from django.test import TestCase
from stocktemplate.models import StockLandingPage
from .models import StaffLandingPage
# Create your tests here.

class TestStaffer404(TestCase):

    def setUp(self):

        stock = StockLandingPage.objects.create()
        stock.set_slug('about')
        stock.save()
        page = StaffLandingPage.objects.create()
        page.set_slug('staff')
        page.set_parent(stock)
        stock.save()

    def test_route_no_staff(self):
        response = self.client.get('/about/staff/foobar/')
        assert response.status_code == 404
