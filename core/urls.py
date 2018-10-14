from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^dashboard/', views.dashboard, name="dashboard"),
    url(r'^parsed/', views.parsed, name="parsed"),
    url(r'^parse', views.parse, name = "parse")
]