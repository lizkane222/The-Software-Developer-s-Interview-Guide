from django.contrib import admin
# from django.contrib.admin import UserAdmin as BaseUserAdmin
# from django.contrib.auth.models import User

# import your models here
from .models import Card, Language, Feature



# class UserAdmin(BaseUserAdmin):
#     inline = (ProfileInline,)



# Register your models here
admin.site.register(Card)
admin.site.register(Language)
admin.site.register(Feature)

# admin.site.register(UserAdmin)
