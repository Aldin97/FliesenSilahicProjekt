from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.gallery_view, name="index"),
    path('submit/', views.index_contact, name='index_post'),
    path("datenschutzerkl#rung", views.datenschutz, name="daten"),
    path("impressum", views.impressum, name="impressum"),

] 
