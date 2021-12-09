from django.urls import path
from currency_app.views import CurrencyRatePlot, CurrencyRateAdd


urlpatterns = [
    # base path to local use/test application is "127.0.0.1:8000/"
    path('', CurrencyRatePlot.as_view(), name='index'),
    # path to local use add/update currency rate "127.0.0.1:8000/update/"
    path('update/', CurrencyRateAdd.as_view(), name='update'),
]