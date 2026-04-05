from django import forms
from .models import Idea

class IdeaForm(forms.ModelForm):
    class Meta:
        model = Idea
        fields = ['title', 'description', 'status']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ex: App de Gestão de Tarefas'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Descreve a tua ideia...'
            }),
            'status': forms.Select(attrs={'class': 'form-select'})
        }
        labels = {
            'title': 'Título da Ideia',
            'description': 'Descrição',
            'status': 'Estado'
        }