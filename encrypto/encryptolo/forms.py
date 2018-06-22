from django import forms

class FormClass(forms.Form):
    name= forms.CharField()
    text= forms.CharField(widget=forms.Textarea)
class FormClass2(forms.Form):
    key= forms.CharField()
    dec_text= forms.CharField()

    