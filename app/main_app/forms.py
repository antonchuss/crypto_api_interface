from django import forms
from .models import TransactionHistory

class RegularTradeForm(forms.Form):
    buy_currency = forms.CharField(
        max_length=50,
        label='Buy currency',
        widget=forms.TextInput(attrs={
            'class': 'form-control currency-autocomplete tradeform-predetermined',
            'id': 'tradeform_buy_currency',
        })
    )

    buy_currency_amount = forms.FloatField(
        label='Buy currency amount',
        widget=forms.NumberInput(attrs={
            'class': 'form-control tradeform-predetermined',
            'id': 'tradeform_buy_amount',
        })
    )

    sell_currency = forms.CharField(
        max_length=50,
        label='Sell currency',
        widget=forms.TextInput(attrs={
            'class': 'form-control currency-autocomplete tradeform-predetermined',
            'id': 'tradeform_sell_currency',
        })
    )

    sell_currency_amount = forms.FloatField(
        label='Sell currency amount',
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'id': 'tradeform_sell_amount',
            'placeholder': 'Fill the other forms to calculate possible sell amount'
        })
    )

class TickerForm(forms.Form):
    currency = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={'class': 'form-control currency-autocomplete'})
    )
