from django.forms import ModelForm
from .models import Card, Language, Feature, Category, Code_Snippet, Image, Text, Concept, Profile, Resource, Definition
from django import forms
# from django.contrib.postgres.forms import SimpleArrayField
# from django.contrib.postgres.fields import ArrayField


# S3_BASE_URL = 'https://s3-us-west-1.amazonaws.com/'
# BUCKET ='devguideassets'


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


class Category_Form(ModelForm):
    name = forms.CharField()

    languages = forms.ModelChoiceField(queryset=Language.objects.all())

    class Meta:
        model = Category
        fields = ["name", "languages"]


class Code_Snippet_Form(ModelForm):
    content = forms.CharField()
    url = forms.CharField()

    class Meta:
        model = Code_Snippet
        fields = ["content", "url"]


class Image_Form(ModelForm):
    name = forms.CharField()
    # url = forms.CharField()
    url = forms.ImageField(required=False, widget=forms.FileInput, label="Upload Image")
    alt_text = forms.CharField()
    creator = forms.CharField()

    class Meta:
        model = Image
        fields = ["name", "url", "alt_text", "creator"]


class Text_Form(ModelForm):
    name = forms.CharField()
    heading = forms.CharField()
    subheading = forms.CharField()
    content = forms.CharField(widget=forms.Textarea, label='')
    creator = forms.CharField()

    class Meta:
        model = Text
        fields = ["name", "heading", "subheading", "content", "creator"]


class Card_Form(ModelForm):
    term = forms.CharField()
    altname = forms.CharField()
    subterms = forms.CharField()
    topic = forms.CharField()
    # img = forms.CharField()
    img = forms.ImageField(required=False, widget=forms.FileInput, label="Upload Image")
    creator = forms.CharField()
    definition = forms.CharField()

    # code_snippets = forms.ModelChoiceField(queryset=Code_Snippet.objects.all(), to_field_name="content")
    # categories = forms.ModelChoiceField(queryset=Category.objects.all(), to_field_name="name")
    # images = forms.ModelChoiceField(queryset=Image.objects.all(), to_field_name="name")
    # resources = forms.ModelChoiceField(queryset=Resource.objects.all(), to_field_name="name")
    # concepts = forms.ModelChoiceField(queryset=Concept.objects.all(), to_field_name="name")
    # texts = forms.ModelChoiceField(queryset=Text.objects.all(), to_field_name="heading")
    # definition = forms.CharField()
    
    class Meta:
        model = Card
        # fields = ['term', "altname", "subterms", "topic", "img", "creator", "code_snippets", "categories", "images", "resources", "concepts", "texts"]
        fields = ['term', "altname", "subterms", "topic", "img", "creator", "definition"]


class Definition_Form(ModelForm):
    content = forms.CharField()
    cards = forms.ModelChoiceField(queryset=Card.objects.all())

    class Meta:
        model = Definition
        fields = ["content", "cards"]


class Language_Form(ModelForm):
    name = forms.CharField()
    stack = forms.CharField()
    when_to_use = forms.CharField()
    best_features = forms.CharField()

    cards = forms.ModelChoiceField(queryset=Card.objects.all())
    code_snippets = forms.ModelChoiceField(queryset=Code_Snippet.objects.all())
    categories = forms.ModelChoiceField(queryset=Category.objects.all())
    images = forms.ModelChoiceField(queryset=Image.objects.all())
    resources = forms.ModelChoiceField(queryset=Resource.objects.all())
    concepts = forms.ModelChoiceField(queryset=Concept.objects.all())
    texts = forms.ModelChoiceField(queryset=Text.objects.all())
    class Meta:
        model = Language
        fields = ["name", "stack", "when_to_use", "best_features", "cards", "code_snippets", "categories", "images", "resources", "concepts", "texts"]


class Concept_Form(ModelForm):
    name = forms.CharField()
    notes = forms.CharField(widget=forms.Textarea, label='')

    cards = forms.ModelChoiceField(queryset=Card.objects.all())
    languages = forms.ModelChoiceField(queryset=Language.objects.all())
    code_snippets = forms.ModelChoiceField(queryset=Code_Snippet.objects.all())
    categories = forms.ModelChoiceField(queryset=Category.objects.all())
    images = forms.ModelChoiceField(queryset=Image.objects.all())
    resources = forms.ModelChoiceField(queryset=Resource.objects.all())
    concepts = forms.ModelChoiceField(queryset=Concept.objects.all())
    texts = forms.ModelChoiceField(queryset=Text.objects.all())
    
    class Meta:
        model = Concept
        fields = ["name", "notes", "creator", "cards", "languages", "code_snippets", "categories", "images", "resources", "texts", ]


class Profile_Form(ModelForm):
    cards = forms.ModelChoiceField(queryset=Card.objects.all())
    languages = forms.ModelChoiceField(queryset=Language.objects.all())
    code_snippets = forms.ModelChoiceField(queryset=Code_Snippet.objects.all())
    categories = forms.ModelChoiceField(queryset=Category.objects.all())
    images = forms.ModelChoiceField(queryset=Image.objects.all())
    resources = forms.ModelChoiceField(queryset=Resource.objects.all())
    concepts = forms.ModelChoiceField(queryset=Concept.objects.all())
    texts = forms.ModelChoiceField(queryset=Text.objects.all())

    class Meta:
        model = Profile
        fields = ["cards", "languages", "code_snippets", "categories", "images", "resources", "concepts", "texts"]


