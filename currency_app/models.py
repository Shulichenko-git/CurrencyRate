from django.db import models


class Currency(models.Model):
    ''' Class of currency. Has two fields: rate and date.
    rate format - decimal number, two decimal places, positive number
    date format - YYYY-MM-DD. User can input today's date and early '''

    rate = models.DecimalField(max_digits=6, decimal_places=2)
    date = models.DateField(help_text='YYYY-MM-DD')

    # def __str__(self):
    #     ''' Presents an instance of Currency class rate=25.00, date=2021-11-05 like '25.00|2021-11-05' '''
    #     return f'{self.rate}|{self.date}'

    def __str__(self):
        ''' Presents an instance of Currency class rate=25.00, date=2021-11-05 like '25.00|2021-11-05' '''
        return '%s|%s' % (self.rate, self.date)
