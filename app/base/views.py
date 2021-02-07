from django.shortcuts import render
from django.views.generic import FormView
from django.contrib.auth.views import LoginView,TemplateView,LogoutView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,authenticate,logout
from django.http import JsonResponse,HttpResponse,HttpResponseRedirect
from django.urls import reverse_lazy
from business.models import Business
from users.models import CustomUser
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
    def post(self,request,*args,**kwargs):
        print(self.request.POST)
        username=request.POST["username"]
        password=request.POST["password"]
        form=AuthenticationForm(username,password)
        permission=CustomUser.objects.filter(business__id=request.POST["business"])
        if permission.exists():
            if form.is_valid():
                login(self.request,form.get_user())
                print(authenticate)
                return HttpResponseRedirect(self.success_url)
            else:
                return HttpResponse("Usuario o contraseña incorrecta.")
        return HttpResponse("No tiene accesos a esa empresa.")
    def form_valid(self,form):
        print("form")
        login(self.request,form.get_user())
        return HttpResponseRedirect(self.success_url)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["business"] = Business.objects.all()
        return context
    
class Logout(LogoutView):
    next_page="/"
