from . import views
from django.urls import path

urlpatterns = [
    path('',
         views.BrokerListView.as_view(),
         name='broker_list'),
    path('create/',
         views.BrokerCreateView.as_view(),
         name='broker_create'
         ),
    path('<int:pk>/edit/',
         views.BrokerUpdateView.as_view(),
         name='broker_update'
         ),
    path('<int:pk>/delete/',
        views.BrokerDeleteView.as_view(),
        name='broker_delete'),
    path('<int:pk>/detail/',
         views.BrokerDetailView.as_view(),
         name='broker_detail'
         ),
    ]