from django.urls import path

from . import views

# app_name = "encyclopedia"
urlpatterns = [
    path("", views.index, name="index"),
    # path("wiki/", views.index, name="index"),
    path("wiki/<str:entry>/", views.wiki, name="wiki"),
    path("search/", views.search, name="search"),
    path("add/", views.add, name="add"),
    # path("edit/", views.edit, name="edit"), 
    path("edit/<str:entry>/", views.edit, name="edit"),
    path("random/", views.random_entry, name="random")
]
