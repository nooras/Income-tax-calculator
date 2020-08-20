from django import forms

class TaxForms(forms.Form):
    age = forms.CharField(required=True)
    income = forms.CharField(required=True)
    investment_amount = forms.CharField(required=True)