from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Workout
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

class WorkoutListView(LoginRequiredMixin, ListView):
    model = Workout
    template_name = 'workouts/workout_list.html'
    context_object_name = 'workouts'

    def get_queryset(self):
        return Workout.objects.filter(user=self.request.user)

class WorkoutDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Workout
    template_name = 'workouts/workout_detail.html'
    context_object_name = 'workout'

    def test_func(self):
        workout = self.get_object()
        return workout.user == self.request.user

class WorkoutCreateView(LoginRequiredMixin, CreateView):
    model = Workout
    fields = ['name', 'description', 'duration', 'calories_burned']
    template_name = 'workouts/workout_form.html'
    success_url = reverse_lazy('workouts:workout_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class WorkoutUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Workout
    fields = ['name', 'description', 'duration', 'calories_burned']
    template_name = 'workouts/workout_form.html'
    success_url = reverse_lazy('workouts:workout_list')

    def test_func(self):
        workout = self.get_object()
        return workout.user == self.request.user

class WorkoutDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Workout
    template_name = 'workouts/workout_confirm_delete.html'
    success_url = reverse_lazy('workouts:workout_list')

    def test_func(self):
        workout = self.get_object()
        return workout.user == self.request.user
