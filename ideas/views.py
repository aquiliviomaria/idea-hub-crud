from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib import messages
from .models import Idea
from .forms import IdeaForm


class IdeaListView(ListView):
    model = Idea
    template_name = 'ideas/idea_list.html'
    context_object_name = 'ideas'
    paginate_by = 10

class IdeaCreateView(CreateView):
    model = Idea
    form_class = IdeaForm
    template_name = 'ideas/idea_form.html'
    success_url = reverse_lazy('idea_list')
    
    def form_valid(self, form):
        messages.success(self.request, 'Ideia criada com sucesso!')
        return super().form_valid(form)

class IdeaUpdateView(UpdateView):
    model = Idea
    form_class = IdeaForm
    template_name = 'ideas/idea_form.html'
    success_url = reverse_lazy('idea_list')
    
    def form_valid(self, form):
        messages.success(self.request, 'Ideia actualizada com sucesso!')
        return super().form_valid(form)

class IdeaDeleteView(DeleteView):
    model = Idea
    template_name = 'ideas/idea_confirm_delete.html'
    success_url = reverse_lazy('idea_list')
    
    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Ideia removida com sucesso!')
        return super().delete(request, *args, **kwargs)

