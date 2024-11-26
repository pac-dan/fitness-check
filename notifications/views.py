from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Notification
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


class NotificationListView(LoginRequiredMixin, ListView):
    model = Notification
    template_name = 'notifications/notification_list.html'
    context_object_name = 'notifications'

    def get_queryset(self):
        return Notification.objects.filter(user=self.request.user)

class NotificationDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Notification
    template_name = 'notifications/notification_detail.html'
    context_object_name = 'notification'

    def test_func(self):
        notification = self.get_object()
        return notification.user == self.request.user

class NotificationCreateView(LoginRequiredMixin, CreateView):
    model = Notification
    fields = ['title', 'message', 'read']
    template_name = 'notifications/notification_form.html'
    success_url = reverse_lazy('notifications:notification_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class NotificationUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Notification
    fields = ['title', 'message', 'read']
    template_name = 'notifications/notification_form.html'
    success_url = reverse_lazy('notifications:notification_list')

    def test_func(self):
        notification = self.get_object()
        return notification.user == self.request.user

class NotificationDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Notification
    template_name = 'notifications/notification_confirm_delete.html'
    success_url = reverse_lazy('notifications:notification_list')

    def test_func(self):
        notification = self.get_object()
        return notification.user == self.request.user
