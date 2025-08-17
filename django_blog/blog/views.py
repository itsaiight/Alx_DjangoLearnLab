from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.models import User
from django.views import View
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')

class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

class ProfileView(LoginRequiredMixin, View):
    template_name = 'blog/profile.html'

    def get(self, request):
        form = ProfileForm(instance=request.user)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = ProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()  
            messages.success(request, "Your profile was updated successfully.")
            return redirect('profile')
        else:
            messages.error(request, "Please correct the errors below.")
        return render(request, self.template_name, {'form': form})

    

'''class CustomLoginView(LoginView):
    template_name = 'relationship_app/login.html'
    

class CustomLogoutView(LogoutView):
    template_name = 'relationship_app/logout.html'''