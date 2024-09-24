from django.urls import path

from subject import views


urlpatterns = [
    path('categories/', views.CategoryListView.as_view(), name='category-list'),
]