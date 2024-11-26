from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Wearable
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

class WearableListView(LoginRequiredMixin, ListView):
    model = Wearable
    template_name = 'wearables/wearable_list.html'
    context_object_name = 'wearables'

    def get_queryset(self):
        return Wearable.objects.filter(user=self.request.user)

class WearableDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Wearable
    template_name = 'wearables/wearable_detail.html'
    context_object_name = 'wearable'

    def test_func(self):
        wearable = self.get_object()
        return wearable.user == self.request.user

class WearableCreateView(LoginRequiredMixin, CreateView):
    model = Wearable
    fields = ['device_name', 'brand', 'model', 'purchase_date', 'notes']
    template_name = 'wearables/wearable_form.html'
    success_url = reverse_lazy('wearables:wearable_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class WearableUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Wearable
    fields = ['device_name', 'brand', 'model', 'purchase_date', 'notes']
    template_name = 'wearables/wearable_form.html'
    success_url = reverse_lazy('wearables:wearable_list')

    def test_func(self):
        wearable = self.get_object()
        return wearable.user == self.request.user

class WearableDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Wearable
    template_name = 'wearables/wearable_confirm_delete.html'
    success_url = reverse_lazy('wearables:wearable_list')

    def test_func(self):
        wearable = self.get_object()
        return wearable.user == self.request.user