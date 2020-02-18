from django.contrib import admin

from .models import (
    UserData,
    Agreement,
    TermsOfService
)
# Register your models here.
admin.register(UserData)
admin.register(Agreement)
admin.register(TermsOfService)