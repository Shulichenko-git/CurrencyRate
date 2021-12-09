from django.contrib.auth.models import AnonymousUser
from django.test import TestCase, Client, RequestFactory
from currency_app.models import Currency
from currency_app.views import CurrencyRateAdd, CurrencyRatePlot


class CurrencyTestCase(TestCase):
    def setUp(self) -> None:
        test_currency1 = Currency.objects.create(id=1, rate=23.23, date='2021-11-01')
        test_currency2 = Currency.objects.create(id=2, rate=24.24, date='2021-11-02')
        test_currency3 = Currency.objects.create(id=3, rate=25.25, date='2021-11-03')

    def test_currency_object_as_str(self):
        currency = Currency.objects.get(id=1)
        expected_object_name = '%s|%s' % (currency.rate, currency.date)
        self.assertEquals(expected_object_name, str(currency))

    def test_str_method(self):
        currency = Currency.objects.get(date='2021-11-01')
        self.assertEquals(str(currency.rate), '23.23')

    def test_index_page_is_ok(self):
        client = Client()
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'currency_app/plot.html')

    def test_update_page_is_ok(self):
        client = Client()
        response = self.client.get('/update/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'currency_app/currency_form.html')

    def test_add_currency_rate_via_factory(self):
        factory = RequestFactory()
        request = factory.get('/update/')
        request.user = AnonymousUser()
        response = CurrencyRateAdd.as_view()(request)
        self.assertEqual(response.status_code, 200)


class CurrencyRatePlotTest(TestCase):
    def setUp(self) -> None:
        test_currency1 = Currency.objects.create(id=1, rate=23.23, date='2021-11-01')

    def test_data_in_context(self):
        request = RequestFactory().get('/')
        view = CurrencyRatePlot()
        view.setup(request)
        context = view.get_context_data()
        self.assertEqual('23.23', str(context['data'][0]['rate']))
        self.assertIn('2021-11-01', context['data'][0]['date'])

