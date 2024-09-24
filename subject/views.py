from rest_framework import views, generics, permissions, status
from rest_framework.response import Response

from django_filters.rest_framework import DjangoFilterBackend

from subject import models, serializers, filters


class CategoryListView(generics.ListAPIView):
    serializer_class = serializers.CategorySerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = filters.CategoryFilter
    queryset = models.Category.objects.all()

