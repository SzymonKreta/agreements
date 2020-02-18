from rest_framework import viewsets
from . import models
from . import serializers


class UserViewset(viewsets.ModelViewSet):
    queryset = models.UserData.objects.all()
    serializer_class = serializers.UserSerializer


class AgreementViewset(viewsets.ModelViewSet):
    queryset = models.Agreement.objects.all()
    serializer_class = serializers.AgreementSerializer


class TermsOfServiceViewset(viewsets.ModelViewSet):
    queryset = models.TermsOfService.objects.all()
    serializer_class = serializers.TermsOfServiceSerializer
