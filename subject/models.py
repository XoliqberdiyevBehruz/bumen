from django.db import models
from django.utils.translation import gettext_lazy as _

from common.models import BaseModel


class Category(BaseModel):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='category/images/%Y/%m/%d')
    logo = models.ImageField(upload_to='category/logos/%Y/%m/%d')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = _('Categories')
        verbose_name = _('Category')


class Lesson(BaseModel):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='category/logo/%Y/%m/%d')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = _('Sub-categories')
        verbose_name = _('Sub-category')


