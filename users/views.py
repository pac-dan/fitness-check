from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from workouts.models import Workout
from goals.models import Goal
from nutrition.models import Nutrition

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

class UserUpdateView(UpdateView):
    model = CustomUser
    fields = ['username', 'email', 'first_name', 'last_name', 'age', 'weight', 'height']
    template_name = 'users/user_form.html'
    success_url = reverse_lazy('users:user_list')

class UserDeleteView(DeleteView):
    model = CustomUser
    template_name = 'users/user_confirm_delete.html'
    success_url = reverse_lazy('users:user_list')

@login_required
def profile(request):
    user = request.user

    #fetch the users data
    workouts = Workout.objects.filter(user=user).order_by('-id')[:5]
    goals = Goal.objects.filter(user=user).order_by('-id')[:5]  
    nutrition_entries = Nutrition.objects.filter(user=user).order_by('-id')[:5]

    context = {
        'workouts':workouts,
        'goals':goals,
        'nutrition_entries':nutrition_entries
    }

    return render(request, 'users/user_profile.html', context)