from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Nutrition
from .forms import NutritionForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

class NutritionListView(LoginRequiredMixin, ListView):
    model = Nutrition
    template_name = 'nutrition/nutrition_list.html'
    context_object_name = 'nutrition_entries'

    def get_queryset(self):
        return Nutrition.objects.filter(user=self.request.user)

class NutritionDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Nutrition
    template_name = 'nutrition/nutrition_detail.html'
    context_object_name = 'nutrition_entry'

    def test_func(self):
        nutrition = self.get_object()
        return nutrition.user == self.request.user

class NutritionCreateView(LoginRequiredMixin, CreateView):
    model = Nutrition
    form_class = NutritionForm
    template_name = 'nutrition/nutrition_form.html'
    success_url = reverse_lazy('nutrition:nutrition_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class NutritionUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Nutrition
    form_class = NutritionForm
    template_name = 'nutrition/nutrition_form.html'
    success_url = reverse_lazy('nutrition:nutrition_list')

    def test_func(self):
        nutrition = self.get_object()
        return nutrition.user == self.request.user

class NutritionDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Nutrition
    template_name = 'nutrition/nutrition_confirm_delete.html'
    success_url = reverse_lazy('nutrition:nutrition_list')

    def test_func(self):
        nutrition = self.get_object()
        return nutrition.user == self.request.user
