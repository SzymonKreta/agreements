from rest_framework import serializers
from . import models


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UserData
        fields = ('__all__')


class TermsOfServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TermsOfService
        fields = ('__all__')


class AgreementSerializer(serializers.ModelSerializer):
    users = UserSerializer(source='user')
    documents = TermsOfServiceSerializer(source='document')
    class Meta:
        model = models.Agreement
        fields = ('__all__')
