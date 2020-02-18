import re


import colander
from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.postgres.fields.jsonb import JSONField

from .schemas import TermsOfServiceSchema
# Create your models here.

def post_code_validator(code):
    if not re.match(r"\d{2}\-\d{3}", code):  # It's polish version
        raise ValidationError("Please put the valid post code")


def validate_terms_of_service_content(content):
    try:
        TermsOfServiceSchema().deserialize(content)
    except colander.Invalid as e:
        raise ValidationError('Valid schema for terms of services is: '
                              '[{"title: "...", "content": "..."}, '
                              '{"title: "...", "content": "..."}, ...]')


class UserData(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    street = models.CharField(max_length=60)
    post_code = models.CharField(validators=[post_code_validator], max_length=6)


class TermsOfService(models.Model):
    created = models.DateTimeField(auto_now=True)
    content = JSONField(validators=[validate_terms_of_service_content])


class Agreement(models.Model):
    signed_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(to=UserData, on_delete=models.SET_NULL, null=True)
    document = models.ForeignKey(to=TermsOfService, on_delete=models.SET_NULL, null=True)
