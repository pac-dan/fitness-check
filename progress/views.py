from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Progress
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

class ProgressListView(LoginRequiredMixin, ListView):
    model = Progress
    template_name = 'progress/progress_list.html'
    context_object_name = 'progress_entries'

    def get_queryset(self):
        return Progress.objects.filter(user=self.request.user)

class ProgressDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Progress
    template_name = 'progress/progress_detail.html'
    context_object_name = 'progress_entry'

    def test_func(self):
        progress = self.get_object()
        return progress.user == self.request.user

class ProgressCreateView(LoginRequiredMixin, CreateView):
    model = Progress
    fields = ['date', 'weight', 'body_fat_percentage', 'notes']
    template_name = 'progress/progress_form.html'
    success_url = reverse_lazy('progress:progress_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class ProgressUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Progress
    fields = ['date', 'weight', 'body_fat_percentage', 'notes']
    template_name = 'progress/progress_form.html'
    success_url = reverse_lazy('progress:progress_list')

    def test_func(self):
        progress = self.get_object()
        return progress.user == self.request.user

class ProgressDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Progress
    template_name = 'progress/progress_confirm_delete.html'
    success_url = reverse_lazy('progress:progress_list')

    def test_func(self):
        progress = self.get_object()
        return progress.user == self.request.user