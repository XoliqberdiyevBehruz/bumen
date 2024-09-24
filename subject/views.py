from rest_framework import views, generics, permissions, status
from rest_framework.response import Response

from django_filters.rest_framework import DjangoFilterBackend

from subject import models, serializers, filters


class CategoryListView(generics.ListAPIView):
    serializer_class = serializers.CategorySerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = filters.CategoryFilter
    queryset = models.Category.objects.all()


class CategoryDetailView(generics.RetrieveAPIView):
    serializer_class = serializers.CategorySerializer
    permission_classes = (permissions.IsAuthenticated,)
    queryset = models.Category.objects.all()

    def get(self, request, *args, **kwargs):
        category = models.Category.objects.get(pk=kwargs['pk'])
        sub_categories = models.Lesson.objects.filter(category=category)
        sub_category_serializer = serializers.LessonSerializer(sub_categories, many=True)
        serializer = serializers.CategorySerializer(category)
        data = {
            'category': {
                'data': serializer.data,
                'lessons': sub_category_serializer.data
            },
        }
        return Response(data)

