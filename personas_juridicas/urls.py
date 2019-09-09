from django.urls import path

from . import views

urlpatterns = [
    path('', views.index_juridicas, name='index_juridicas'),
    path('nuevo/', views.juridicas_view, name='juridicas_view'),
    path("ajax/load-ciudades/",views.load_ciudades, name="ajax_load_ciudades"),
]