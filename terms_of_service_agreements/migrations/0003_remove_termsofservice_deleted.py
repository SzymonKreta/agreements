# Generated by Django 3.0.3 on 2020-02-18 17:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('terms_of_service_agreements', '0002_auto_20200218_1709'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='termsofservice',
            name='deleted',
        ),
    ]
