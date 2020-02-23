import re

import colander
from django.contrib.postgres.fields.jsonb import JSONField
from django.core.exceptions import ValidationError
from django.db import models

from .schemas import TermsOfServiceSchema


def post_code_validator(code):
    if not re.match(r"\d{2}-\d{3}", code):  # It's polish version
        raise ValidationError("Please put the valid post code")


def validate_terms_of_service_content(content):
    try:
        TermsOfServiceSchema().deserialize(content)
    except colander.Invalid:
        raise ValidationError('Valid schema for terms of services is: '
                              '[{"title: "...", "content": "..."}, '
                              '{"title: "...", "content": "..."}, ...]')


class UserData(models.Model):
    first_name = models.CharField(max_length=30,
                                  help_text="str: user first name")
    last_name = models.CharField(max_length=150,
                                 help_text="str: user last name")
    street = models.CharField(max_length=60,
                              help_text="str: street name of user's home address")
    post_code = models.CharField(validators=[post_code_validator], max_length=6,
                                 help_text="str: valid post code: dd-ddd")


class TermsOfService(models.Model):
    created = models.DateTimeField(auto_now=True,
                                   help_text="datetime: time when document was created")
    content = JSONField(validators=[validate_terms_of_service_content],
                        help_text="json: json that contains list of dictionaries"
                        '{"title": <paragraph title>. "content": <paragraph content>')


class Agreement(models.Model):
    signed_at = models.DateTimeField(auto_now=True,
                                     help_text="datetime: time when agreement was signed")
    user = models.ForeignKey(to=UserData, on_delete=models.SET_NULL, null=True,
                             help_text="valid user schema endpoint json object")
    document = models.ForeignKey(to=TermsOfService, on_delete=models.SET_NULL, null=True,
                                 help_text="valid terms endpoint schema json object")
