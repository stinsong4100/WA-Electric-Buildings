from django.urls import path

from . import views

app_name = 'eBmap'
urlpatterns = [
#    path('', views.index, name='index'),
    path('', views.BuildingList.as_view(), name='index'),
    path('building-list/', views.BuildingList.as_view(), name='building-list'),
]
