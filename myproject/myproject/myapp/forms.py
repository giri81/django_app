# -*- coding: utf-8 -*-

from django import forms
from myproject.myapp.models import SourceDocument

class SourceDocumentForm(forms.Form):
    docfile = forms.FileField(
        label='Select a file', 
    )



