from django.db import models
from django.urls import reverse

class Idea(models.Model):
    STATUS_CHOICES = [
        ('new', 'Nova'),
        ('progress', 'Em Progresso'),
        ('done', 'Concluída'),
        ('archived', 'Arquivada'),
    ]
    
    title = models.CharField(max_length=100, verbose_name='Título')
    description = models.TextField(verbose_name='Descrição')
    status = models.CharField(
        max_length=20, 
        choices=STATUS_CHOICES, 
        default='new',
        verbose_name='Status'
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Criada em')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Actualizada em')
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Ideia'
        verbose_name_plural = 'Ideias'
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('idea_list')