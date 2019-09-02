from django import forms

class sentform(forms.Form):
    name=forms.CharField(max_length=80,widget=forms.TextInput(attrs={'class':'Form-control'}))
    email = forms.CharField(max_length=80, widget=forms.TextInput(attrs={'class': 'Form-control'}))
    subject= forms.CharField(max_length=80, widget=forms.TextInput(attrs={'class': 'Form-control'}))
    message = forms.CharField(max_length=80, widget=forms.TextInput(attrs={'row':8,'cols':70}))