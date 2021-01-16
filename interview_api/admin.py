from django.contrib import admin
# from django.contrib.admin import UserAdmin as BaseUserAdmin
# from django.contrib.auth.models import User

# import your models here
from .models import Card, Language, Feature, Category, Code_Snippet, Image, Resource, Text, Definition, Concept, Profile



# class UserAdmin(BaseUserAdmin):
#     inline = (ProfileInline,)



# Register your models here
admin.site.register(Card)
admin.site.register(Language)
admin.site.register(Feature)
admin.site.register(Category)
admin.site.register(Code_Snippet)
admin.site.register(Image)
admin.site.register(Resource)
admin.site.register(Text)
admin.site.register(Definition)
admin.site.register(Concept)
admin.site.register(Profile)

# admin.site.register(UserAdmin)
