from . import views
from django.urls import path

urlpatterns = [
    path('',
         views.FeatureListView.as_view(),
         name='feature_list'),
    path('create/',
         views.FeatureCreateView.as_view(),
         name='feature_create'
         ),
    path('<int:pk>/edit/',
         views.FeatureUpdateView.as_view(),
         name='feature_update'
         ),
    ]