from django.db import models
import string, random
# from django.contrib.postgres.fields import ArrayField
# from django.contrib.postgres.forms import SimpleArrayField
from django.urls import reverse

from django.db.models.fields import (
    DateField, DateTimeField, DurationField, Field, IntegerField, TimeField,
)
from django.db.models.lookups import (
    Transform, YearExact, YearGt, YearGte, YearLt, YearLte,
)

# Create your database models here.

    # ADMIN ONLY MODEL
class Feature(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, unique=True)
    external_resource = models.CharField(max_length=100, blank=True, default="", unique=False)
    notes = models.CharField(max_length=1000, default="", blank=True, unique=False)
    page = models.CharField(max_length=100, default="", blank=True, unique=False)
    stack_field = models.CharField(max_length=100, default="", blank=True, unique=False)
    is_complete = models.BooleanField(null=False, default=False)
    kind = models.CharField(max_length=8, default="Feature", editable=False)
    updated_at = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return f"[{self.name}] lookup {self.external_resource}. Use @ : {self.page} on the {self.stack_field}. Complete?: {self.is_complete}"


class Category(models.Model):
    name = models.CharField(max_length=100, default="", blank=True, unique=True)
    kind = models.CharField(max_length=8, default="Category", editable=False)

    # many to many w/ Concept Model
    # many to many w/ Card Model
    # many to many w/ Language Model

    def __str__(self):
            return f"{self.name} kind: {self.kind}"


class Code_Snippet(models.Model):
    name = models.CharField(max_length=3000, default="", blank=True, unique=False)
    content = models.CharField(max_length=3000, default="", blank=True, unique=False)
    url = models.CharField(max_length=3000, default="", blank=True, unique=False)
    creator = models.CharField(max_length=1000, default="", blank=True, unique=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)
    kind = models.CharField(max_length=13, default="Code_Snippet", editable=False)
    
    # many to many w/ Card Model
    # many to many w/ Concept Model
    # many to many w/ Language Model

    def __str__(self):
        return f"{self.content} kind: {self.kind}"


class Image(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, unique=False) 
    url = models.CharField(max_length=200, default="", blank=True, unique=False)
    # fileSrc = models.ImageField(null=True, blank= True, upload_to = 'images/', default='media/stockphotos/default_icon.png')
    alt_text = models.CharField(max_length=100, default="", blank=True, unique=False)
    creator = models.CharField(max_length=1000, default="", blank=True, unique=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)
    kind = models.CharField(max_length=5, default="Image", editable=False)
    
    # many to many w/ Card Model
    # many to many w/ Concept Model
    # many to many w/ Language Model

    def __str__(self):
        return f"{self.url} kind: {self.kind}"


class Resource(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, unique=True)
    url = models.CharField(max_length=100, default="", blank=True, unique=False)
    creator = models.CharField(max_length=1000, default="", blank=True, unique=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)
    kind = models.CharField(max_length=8, default="Resource", editable=False)
    
    # many to many w/ Card Model
    # many to many w/ Concept Model
    # many to many w/ Language Model

    def __str__(self):
            return f"{self.name} : {self.url}, kind: {self.kind}"


class Text(models.Model):
    heading = models.CharField(max_length=50, null=False, blank=False, unique=True)
    subheading = models.CharField(max_length=75, default="", blank=True, unique=False)
    content = models.TextField(max_length=5000, default="", blank=True, unique=False)
    creator = models.CharField(max_length=100, default="", blank=True, unique=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)
    kind = models.CharField(max_length=4, default="Text", editable=False)
    
    # many to many w/ Card Model
    # many to many w/ Concept Model
    # many to many w/ Language Model
    
    def __str__(self):
        return f"{self.heading} : {self.subheading} by: {self.creator} kind: {self.kind}"



class Card(models.Model):
    term = models.CharField(max_length=30, null=False, blank=False, unique=True)
    altname = models.CharField(max_length=100, blank=True, default="", unique=True)
    subterms = models.CharField(max_length=200, blank=True, default="", unique=False)
    topic = models.CharField(max_length=200, blank=True, default="", unique=False)
    users_can_add_data = models.BooleanField(null=False, default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)
    img = models.CharField(max_length=200, default="", blank=True, unique=False)
    creator = models.CharField(max_length=1000, default="", blank=True, unique=False)
    kind = models.CharField(max_length=4, default="Card", editable=False)
    # definition = models.CharField(max_length=200, default="", blank=True, unique=False)

    code_snippets = models.ManyToManyField(Code_Snippet)
    categories = models.ManyToManyField(Category)
    images = models.ManyToManyField(Image)
    resources = models.ManyToManyField(Resource)
    texts = models.ManyToManyField(Text)
    # many to many w/ Concept Model

    def __str__(self):
        return f"{self.term} : {self.creator} kind: {self.kind}"


class Definition(models.Model):
    content = models.CharField(max_length=3000, null=False, blank=False, unique=False)
    kind = models.CharField(max_length=10, default="Definition", editable=False)
    updated_at = models.DateTimeField(auto_now=True, blank=True)

    cards = models.ForeignKey(Card, on_delete=models.CASCADE)

    def __str__(self):
            return f"{self.content} : [{self.cards}] kind: {self.kind}"



class Language(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False, unique=True)
    stack = models.CharField(max_length=30, default="", blank=True, unique=False)
    when_to_use = models.CharField(max_length=500, default="", blank=True, unique=False)
    best_features = models.CharField(max_length=200, default="", blank=True, unique=False)
    kind = models.CharField(max_length=8, default="Language", editable=False)
    updated_at = models.DateTimeField(auto_now=True, blank=True)

    cards = models.ManyToManyField(Card)
    code_snippets = models.ManyToManyField(Code_Snippet)
    categories = models.ManyToManyField(Category)
    images = models.ManyToManyField(Image)
    resources = models.ManyToManyField(Resource)
    texts = models.ManyToManyField(Text) 

    def __str__(self):
        return f"{self.name}: is a part of the {self.stack} stack. kind: {self.kind}"

class Concept(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, unique=True)
    notes = models.TextField(max_length=5000, default="", blank=True, unique=False)
    creator = models.CharField(max_length=1000, default="", blank=True, unique=False)
    kind = models.CharField(max_length=7, default="Concept", editable=False)
    updated_at = models.DateTimeField(auto_now=True, blank=True)

    cards = models.ManyToManyField(Card)
    languages = models.ManyToManyField(Language)
    code_snippets = models.ManyToManyField(Code_Snippet)
    categories = models.ManyToManyField(Category)
    images = models.ManyToManyField(Image)
    resources = models.ManyToManyField(Resource)
    texts = models.ManyToManyField(Text) 

    def __str__(self):
        return f"{self.name} : {self.notes} kind: {self.kind}"


class Profile(models.Model):
    saved_items = models.BooleanField(null=False, default=False)
    removed_items = models.BooleanField(null=False, default=False)
    review_now = models.BooleanField(null=False, default=False)
    review_later = models.BooleanField(null=False, default=False)
    kind = models.CharField(max_length=7, default="Profile", editable=False)
    updated_at = models.DateTimeField(auto_now=True, blank=True)

    cards = models.ManyToManyField(Card)
    languages = models.ManyToManyField(Language)
    code_snippets = models.ManyToManyField(Code_Snippet)
    categories = models.ManyToManyField(Category)
    images = models.ManyToManyField(Image)
    resources = models.ManyToManyField(Resource)
    concepts = models.ManyToManyField(Concept)
    texts = models.ManyToManyField(Text)

    def __str__(self):
        return f"CARDS: {self.cards}. LANGUAGES: {self.languages.name}. CODE: {self.code_snippets}. Categories {self.categories} {self.images} {self.resources} {self.concepts} {self.texts} kind: {self.kind}"