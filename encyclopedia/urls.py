from django.urls import path

from . import views
name_app= "encyclopedia"
urlpatterns = [
    path("", views.index, name="index"),
    path("entry/<str:title>", views.entry, name="entry"),
    path("search", views.search, name="search"),
    path("create", views.create, name="create"),
    path("edit/<str:title>", views.edit, name="edit"),
    path("random", views.random_title, name="random"),
]
