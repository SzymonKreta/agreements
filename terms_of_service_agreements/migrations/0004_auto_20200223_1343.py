# Generated by Django 3.0.3 on 2020-02-23 12:43

import django.contrib.postgres.fields.jsonb
import django.db.models.deletion
from django.db import migrations, models

import terms_of_service_agreements.models


class Migration(migrations.Migration):

    dependencies = [
        ('terms_of_service_agreements', '0003_remove_termsofservice_deleted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agreement',
            name='document',
            field=models.ForeignKey(help_text='valid terms endpoint schema json object', null=True, on_delete=django.db.models.deletion.SET_NULL, to='terms_of_service_agreements.TermsOfService'),
        ),
        migrations.AlterField(
            model_name='agreement',
            name='signed_at',
            field=models.DateTimeField(auto_now=True, help_text='datetime: time when agreement was signed'),
        ),
        migrations.AlterField(
            model_name='agreement',
            name='user',
            field=models.ForeignKey(help_text='valid user schema endpoint json object', null=True, on_delete=django.db.models.deletion.SET_NULL, to='terms_of_service_agreements.UserData'),
        ),
        migrations.AlterField(
            model_name='termsofservice',
            name='content',
            field=django.contrib.postgres.fields.jsonb.JSONField(help_text='json: json that contains list of dictionaries{"title": <paragraph title>. "content": <paragraph content>', validators=[terms_of_service_agreements.models.validate_terms_of_service_content]),
        ),
        migrations.AlterField(
            model_name='termsofservice',
            name='created',
            field=models.DateTimeField(auto_now=True, help_text='datetime: time when document was created'),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='first_name',
            field=models.CharField(help_text='str: user first name', max_length=30),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='last_name',
            field=models.CharField(help_text='str: user last name', max_length=150),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='post_code',
            field=models.CharField(help_text='str: valid post code: dd-ddd', max_length=6, validators=[terms_of_service_agreements.models.post_code_validator]),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='street',
            field=models.CharField(help_text="str: street name of user's home address", max_length=60),
        ),
    ]
