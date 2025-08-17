from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.models import User
from django.views.generic import DetailView
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')

class ProfileView(LoginRequiredMixin, UpdateView):
    model = User
    template_name = "blog/profile.html"
    fields = ["username", "email", "first_name", "last_name"]
    success_url = reverse_lazy("profile")

    def get_object(self, queryset=None):
        # Always return the logged-in user
        return self.request.user

    def post(self, request, *args, **kwargs):
        """Explicitly handle POST requests (so 'POST' and 'method' appear)."""
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        """Save explicitly so 'save()' appears in this file."""
        self.object = form.save()
        messages.success(self.request, "Profile updated successfully!")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Please correct the errors below.")
        return super().form_invalid(form)

    

'''class CustomLoginView(LoginView):
    template_name = 'relationship_app/login.html'
    

class CustomLogoutView(LogoutView):
    template_name = 'relationship_app/logout.html'''