from django.contrib import admin

from .models import Agreement, TermsOfService, UserData

# Register your models here.
admin.register(UserData)
admin.register(Agreement)
admin.register(TermsOfService)
