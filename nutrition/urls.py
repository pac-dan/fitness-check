from django.urls import path
from . import views

app_name = 'nutrition'

urlpatterns = [
    path('', views.NutritionListView.as_view(), name='nutrition_list'),
    path('create/', views.NutritionCreateView.as_view(), name='nutrition_create'),
    path('<int:pk>/', views.NutritionDetailView.as_view(), name='nutrition_detail'),
    path('<int:pk>/update/', views.NutritionUpdateView.as_view(), name='nutrition_update'),
    path('<int:pk>/delete/', views.NutritionDeleteView.as_view(), name='nutrition_delete'), 
]