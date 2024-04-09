from django.shortcuts import render
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from .models import Note
from .forms import FormNote
from django.urls import reverse_lazy

# Create your views here.

class HomeView(ListView):
    template_name = "front/index.html"
    model = Note
    context_object_name = "notes"

class CreateNote(CreateView):
    template_name = "front/create-note.html"
    model = Note
    form_class = FormNote
    context_object_name = "note"
    success_url = reverse_lazy("index")

class UpdateNote(UpdateView):
    template_name = "front/update-note.html"
    model = Note
    fields = "__all__"
    context_object_name = "note"
    success_url = reverse_lazy("index")

class DeleteNote(DeleteView):
    template_name = "front/delete-note.html"
    model = Note
    context_object_name = "note"
    success_url = reverse_lazy("index")


