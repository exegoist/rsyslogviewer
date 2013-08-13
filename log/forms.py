from django import forms

class SearchField(forms.Form):
    q = forms.CharField(label='q',max_length=100, required=False)
