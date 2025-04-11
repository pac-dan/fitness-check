from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Workout
from .forms import WorkoutForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages

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
    form_class = WorkoutForm
    template_name = 'workouts/workout_form.html'
    success_url = reverse_lazy('workouts:workout_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, 'Workout created successfully!')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Error creating workout. Please check the form.')
        return super().form_invalid(form)

class WorkoutUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Workout
    form_class = WorkoutForm
    template_name = 'workouts/workout_form.html'
    success_url = reverse_lazy('workouts:workout_list')

    def test_func(self):
        workout = self.get_object()
        return workout.user == self.request.user

    def form_valid(self, form):
        messages.success(self.request, 'Workout updated successfully!')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Error updating workout. Please check the form.')
        return super().form_invalid(form)

class WorkoutDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Workout
    template_name = 'workouts/workout_confirm_delete.html'
    success_url = reverse_lazy('workouts:workout_list')

    def test_func(self):
        workout = self.get_object()
        return workout.user == self.request.user

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Workout deleted successfully!')
        return super().delete(request, *args, **kwargs)
