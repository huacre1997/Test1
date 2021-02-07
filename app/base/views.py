from django.shortcuts import render
from django.views.generic import FormView
from django.contrib.auth.views import LoginView,TemplateView,LogoutView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,authenticate,logout
from django.http import JsonResponse,HttpResponse,HttpResponseRedirect
from django.urls import reverse_lazy
class IndexView(TemplateView):
    template_name="home.html"
class Login(FormView):
    template_name = 'login.html'
    form_class=AuthenticationForm
    success_url=reverse_lazy("base:home")
    def dispatch(self,request,*args, **kwargs):
        print(request.user)
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.success_url)
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self,form):
        print("form")
        login(self.request,form.get_user())
        return HttpResponseRedirect(self.success_url)

class Logout(LogoutView):
    next_page="/"
