import datetime
from django import forms
from django.core.exceptions import ValidationError
from currency_app.models import Currency


class CurrencyRateAddForm(forms.ModelForm):
    '''Form class for add/update of currency rate to database.
    Еру form has fields rate, date linked with Currency model.'''

    class Meta:
        model = Currency
        fields = ['rate', 'date']

    def clean_date(self):
        '''Validate date at the form. Date can't be from future!'''
        date = self.cleaned_data['date']
        if date > datetime.date.today():
            raise ValidationError('Enter the date before the future!')
        return date

    def clean_rate(self):
        '''Validate rate at the form. The rate has to be a positive number.'''
        rate = self.cleaned_data['rate']
        if rate <= 0:
            raise ValidationError('Enter positive rate!')
        return rate
