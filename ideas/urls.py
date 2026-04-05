from django.urls import path
from . import views

urlpatterns = [
    path('', views.IdeaListView.as_view(), name='idea_list'),
    path('criar/', views.IdeaCreateView.as_view(), name='idea_create'),
    path('editar/<int:pk>/', views.IdeaUpdateView.as_view(), name='idea_update'),
    path('apagar/<int:pk>/', views.IdeaDeleteView.as_view(), name='idea_delete'),
]