from . import views
from django.urls import path

urlpatterns = [
    path('',
         views.RealEstateListView.as_view(),
         name='real_estate_list'),
    path('create/',
         views.RealEstateCreateView.as_view(),
         name='real_estate_create'),
    path('<int:pk>/',
         views.RealEstateDetailView.as_view(),
         name='real_estate_detail'),
    path('<int:pk>/edit/',
        views.RealEstateUpdateView.as_view(),
        name='real_estate_update'),
    path('<int:pk>/delete/',
        views.RealEstateDeleteView.as_view(),
        name='real_estate_delete'),
]