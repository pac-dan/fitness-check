from django.urls import path
from . import views

app_name = 'progress'

urlpatterns = [
    path('', views.ProgressListView.as_view(), name='progress_list'),
    path('create/', views.ProgressCreateView.as_view(), name='progress_create'),
    path('<int:pk>/', views.ProgressDetailView.as_view(), name='progress_detail'),
    path('<int:pk>/update/', views.ProgressUpdateView.as_view(), name='progress_update'),
    path('<int:pk>/delete/', views.ProgressDeleteView.as_view(), name='progress_delete'),
]