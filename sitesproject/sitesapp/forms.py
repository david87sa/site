from django import forms

class ConFirmForm(forms.Form):
    name = forms.CharField()
    confirmed = forms.CharField()
