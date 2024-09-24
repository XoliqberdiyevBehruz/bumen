from rest_framework import serializers

from subject import models


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = ('id', 'name', 'image', 'logo')
        read_only_fields = ('id',)


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = ('id', 'name', 'logo')
