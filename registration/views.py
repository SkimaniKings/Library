from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from .forms import CustomUserCreationForm
from django.shortcuts import render

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration.html'
    
# class LoginView(CreateView):
#     template_name = 'login.html'
    
    
    
# def registration(request):
#     return render(request, 'registration.html')

def login(request):
    return render(request, 'login.html')
