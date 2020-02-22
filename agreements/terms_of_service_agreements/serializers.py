from rest_framework import serializers
from . import models


class TermsOfServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TermsOfService
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UserData
        fields = '__all__'


class AgreementSerializer(serializers.ModelSerializer):
    users = UserSerializer(source='user', read_only=True)
    documents = TermsOfServiceSerializer(source='document', read_only=True)
    class Meta:
        model = models.Agreement
        fields = '__all__'
