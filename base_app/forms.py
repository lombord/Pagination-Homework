from django import forms

from .models import Vacancy, Language, Company, STATUSES

form_stats = [('', 'Any')] + STATUSES


class SearchForm(forms.Form):
    search = forms.CharField(widget=forms.TextInput(
        attrs={'type': 'search'}), required=False)
    languages = forms.ModelChoiceField(
        queryset=Language.objects.all(), required=False)

    company = forms.ModelChoiceField(queryset=Company.objects,
                                     required=False, empty_label='Any')
    status = forms.ChoiceField(choices=form_stats,
                               required=False)
