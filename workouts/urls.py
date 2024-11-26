from django.urls import path
from . import views

app_name = 'workouts'

urlpatterns = [
    path('', views.WorkoutListView.as_view(), name='workout_list'),
    path('create/', views.WorkoutCreateView.as_view(), name='workout_create'),
    path('<int:pk>/', views.WorkoutDetailView.as_view(), name='workout_detail'),
    path('<int:pk>/update/', views.WorkoutUpdateView.as_view(), name='workout_update'),
    path('<int:pk>/delete/', views.WorkoutDeleteView.as_view(), name='workout_delete'),
]