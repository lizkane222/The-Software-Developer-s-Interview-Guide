from django.forms import ModelForm
from .models import Card, Language, Feature
from django import forms


class Card_Form(ModelForm):
    term = forms.CharField()
    altname = forms.CharField()
    subterms = forms.CharField()
    definitions = forms.ArrayField()
    category = forms.ArrayField()
    topic = forms.CharField()

    class Meta:
        model = Card
        fields = ['term', "altname", "subterms", "definitions", "category", "topic",]

class Language_Form(ModelForm):
    name = forms.CharField()
    stack = forms.CharField()
    when_to_use = forms.CharField()
    best_features = forms.CharField()

    class Meta:
        model = Language
        fields = ["name", "stack", "when_to_use", "best_features"]


class Feature_Form(ModelForm):
    name = forms.CharField()
    external_resource = forms.CharField()
    notes = forms.CharField()
    page = forms.CharField()
    stack_field = forms.CharField()
    is_complete = forms.BooleanField()

    class Meta:
        model = Feature
        fields = ["name", "external_resource", "notes", "page", "stack_field", "is_complete"]