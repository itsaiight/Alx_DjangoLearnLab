from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import CreateView
from django.views.generic import DetailView

# Create your views here.
class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')

class ProfileView(DetailView):
    def get(self, request):
        if request.user.is_authenticated:
            return render(request, 'blog/profile.html', {'user': request.user})
        else:
            return redirect('login')

    

'''class CustomLoginView(LoginView):
    template_name = 'relationship_app/login.html'
    

class CustomLogoutView(LogoutView):
    template_name = 'relationship_app/logout.html'''