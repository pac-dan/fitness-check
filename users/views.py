from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import UserUpdateForm
from workouts.models import Workout
from goals.models import Goal
from nutrition.models import Nutrition
from django.contrib.auth import get_user_model
from django import forms

CustomUser = get_user_model()

class UserListView(ListView):
    model = CustomUser
    template_name = 'users/user_list.html'
    context_object_name = 'users'

class UserDetailView(DetailView):
    model = CustomUser
    template_name = 'users/user_detail.html'
    context_object_name = 'user'

class UserCreateView(CreateView):
    model = CustomUser
    form_class = UserCreationForm
    template_name = 'users/user_form.html'
    success_url = reverse_lazy('users:user_list')

class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = CustomUser
    form_class = UserUpdateForm
    template_name = 'users/user_update.html'
    success_url = reverse_lazy('users:profile')  # Adjust as needed

    def get_object(self, queryset=None):
        return self.request.user

class UserDeleteView(DeleteView):
    model = CustomUser
    template_name = 'users/user_confirm_delete.html'
    success_url = reverse_lazy('users:user_list')

@login_required
def profile(request):
    user = request.user

    #fetch the users data
    workouts = Workout.objects.filter(user=user).order_by('-id')[:3]
    goals = Goal.objects.filter(user=user).order_by('-id')[:3]  
    nutrition_entries = Nutrition.objects.filter(user=user).order_by('-id')[:3]

    context = {
        'workouts':workouts,
        'goals':goals,
        'nutrition_entries':nutrition_entries
    }

    return render(request, 'users/user_profile.html', context)

