from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import FormView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View

class LoginView(FormView):
    template_name = 'registration/login.html'
    form_class = AuthenticationForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(self.request, user)
            return super().form_valid(form)
        else:
            form.add_error(None, "Invalid username or password")
            return self.form_invalid(form)

class SignupView(CreateView):
    template_name = 'registration/signup.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('login')

class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'commute/home.html'
    login_url = '/login/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['username'] = self.request.user.username
        return context

class UserTypeSelectionView(View):
    def get(self, request):
        return render(request, 'commuter/user_type_selection.html')
    
class AboutView(LoginRequiredMixin, TemplateView):
    template_name = 'commute/about.html'
    login_url = '/login/'

class ContactView(LoginRequiredMixin, TemplateView):
    template_name = 'commute/contact.html'
    login_url = '/login/'

class GetaquoteView(LoginRequiredMixin, TemplateView):
    template_name = 'commute/get-a-quote.html'
    login_url = '/login/'

class SampleinnerpageView(LoginRequiredMixin, TemplateView):
    template_name = 'commute/sample-inner-page.html'
    login_url = '/login/'

class ServicedetailsView(LoginRequiredMixin, TemplateView):
    template_name = 'commute/service-details.html'
    login_url = '/login/'