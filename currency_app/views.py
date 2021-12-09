from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView
from currency_app.forms import CurrencyRateAddForm
from currency_app.models import Currency


class CurrencyRatePlot(TemplateView):
    '''Linked the template with Currency model
    and get data for currency chart from DB.
    Ordering data by date.'''

    model = Currency
    template_name = 'currency_app/plot.html'

    def get_context_data(self, **kwargs):
        '''get data from Currency and return contex'''
        context = super().get_context_data(**kwargs)
                                # from context below we make render a chart at plot.html
        context['data'] = [
            {
                'rate': currency.rate,
                'date': currency.date.isoformat()
            }
            for currency in Currency.objects.all().order_by('date')
        ]
        return context


class CurrencyRateAdd(FormView):
    '''Clacc form for add/update currency rate'''
    model = Currency
    form_class = CurrencyRateAddForm
    template_name = ('currency_app/currency_form.html')
    success_url = reverse_lazy('index')
    fields = ['rate', 'date']

    def post(self, request, *args, **kwargs):
        '''Method checks if value of date already exists in Currency,
         then we UPDATE the rate value. If value of date doesn't exist,
         then we CREATE the new rate'''
        form = CurrencyRateAddForm(request.POST)
        if form.is_valid():
            currency = Currency.objects.filter(date=form.cleaned_data['date'])
            if currency.exists() and currency.count() == 1:
                # Update
                currency.update(rate=form.cleaned_data['rate'])
            else:
                # Create
                currency.create(rate=form.cleaned_data['rate'], date=form.cleaned_data['date'])
            return redirect('index')
        else:
            return render(request, 'currency_app/currency_form.html', {'form': form})
