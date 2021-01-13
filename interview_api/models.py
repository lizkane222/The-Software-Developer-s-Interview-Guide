from django.db import models
import string, random
from django.contrib.postgres.fields import ArrayField


def generate_unique_code():
    length = 8

    while True:
        code = ''.join(random.choices(string.ascii_uppercase, k=length))
        if Card.objects.filter(code=code).count() == 0:
            break

    return code

# Create your database models here.

# Cards of vocabulary terms
class Card(models.Model):
    term = models.CharField(max_length=30, default="", unique=True)
    altname = models.CharField(max_length=100, default="", unique=True)
    subterms = models.CharField(max_length=200, default="", unique=False)
    definitions = ArrayField(
        ArrayField(
            models.CharField(max_length=3000, default="", blank=True, unique=False),
            size=100
        ),
        size=50,
    ),
    category = models.CharField(max_length=200, default="", unique=False)
    topic = models.CharField(max_length=200, default="", unique=False)
    creator = models.CharField(max_length=1000, default="", unique=False)
    codeSnippet = ArrayField(
        ArrayField(
            models.CharField(max_length=3000, default="", blank=True, unique=False),
            size=100
        ),
        size=50,
    ),
    users_can_add_data = models.BooleanField(null=False, default=True)
    created_at = models.DateTimeField(auto_now_add=True),

    def __str__(self):
        return f"{self.term} : {self.definitions}, Category: {self.category}, Creator: {self.creator}"

# Software Languages
class Language(models.Model):
    name = models.CharField(max_length=50, default="", unique=True)
    stack = models.CharField(max_length=30, default="", unique=False)
    when_to_use = models.CharField(max_length=500, default="", unique=True)
    best_features = models.CharField(max_length=200, default="", unique=True)

    def __str__(self):
        return f"{self.name}: is a part of the {self.stack} stack."

# ADMIN ONLY MODEL
class Feature(models.Model):
    name = models.CharField(max_length=100, default="", unique=True)
    external_resource = models.CharField(max_length=100, default="", unique=False)
    notes = models.CharField(max_length=1000, default="", unique=False)
    page = models.CharField(max_length=100, default="", unique=False)
    stack_field = models.CharField(max_length=100, default="", unique=False)
    is_complete = models.BooleanField(null=False, default=False)

    def __str__(self):
        return f"[{self.name}] lookup {self.external_resource}. Use @ : {self.page} on the {self.stack_field}. Complete?: {self.is_complete}"
