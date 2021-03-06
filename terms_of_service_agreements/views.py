from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination

from . import models, serializers


class StandardPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'size'
    max_page_size = 100


class TermsOfServiceDefaultPagination(StandardPagination):
    page_size = 1
    max_page_size = 10


class UserViewset(viewsets.ModelViewSet):
    queryset = models.UserData.objects.all()
    serializer_class = serializers.UserSerializer
    pagination_class = StandardPagination
    filterset_fields = ('identifier',)
    ordering = ['id']
    http_method_names = ['get', 'post', 'head']


class AgreementViewset(viewsets.ModelViewSet):
    queryset = models.Agreement.objects.all()
    serializer_class = serializers.AgreementSerializer
    pagination_class = StandardPagination
    ordering = ['id']
    filterset_fields = ('user', 'user__identifier')


class TermsOfServiceViewset(viewsets.ModelViewSet):
    queryset = models.TermsOfService.objects.all()
    serializer_class = serializers.TermsOfServiceSerializer
    pagination_class = TermsOfServiceDefaultPagination
    ordering = ['id']
    http_method_names = ['get', 'post', 'head']
