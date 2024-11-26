from django.urls import path
from . import views

app_name = 'wearables'

urlpatterns = [
    path('', views.WearableListView.as_view(), name='wearable_list'),
    path('create/', views.WearableCreateView.as_view(), name='wearable_create'),
    path('<int:pk>/', views.WearableDetailView.as_view(), name='wearable_detail'),
    path('<int:pk>/update/', views.WearableUpdateView.as_view(), name='wearable_update'),
    path('<int:pk>/delete/', views.WearableDeleteView.as_view(), name='wearable_delete'),
]