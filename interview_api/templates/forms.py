from django.forms import ModelForm
from .models import Card, Language



class Card_Form(ModelForm):
    term = forms.CharField()
    altname = forms.CharField()
    subterms = forms.CharField()
    definitions = forms.TextField()
    category = forms.CharField()
    topic = forms.CharField()

    class Meta:
        model = Card
        fields = ['term', "altname", "subterms", "definitions", "category", "topic",]

class Language(ModelForm):
    name = forms.CharField()
    stack = forms.CharField()
    when_to_use = forms.CharField()
    best_features = forms.CharField()

    class Meta:
        model = Language
        fields = ["name", "stack", "when_to_use", "best_features"]

