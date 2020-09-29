from django import forms


class MapboxSearchForm(forms.Form):
    search_text = forms.CharField(label="Search Text")