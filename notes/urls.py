from django.urls import path
from front import views

urlpatterns = [
    path("", views.HomeView.as_view(), name="index"),
    path("create/", views.CreateNote.as_view(), name="create_note"),
    path("update/<pk>", views.UpdateNote.as_view(), name="update_note"),
    path("delete/<pk>", views.DeleteNote.as_view(), name="delete_note")
]
