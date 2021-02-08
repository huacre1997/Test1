from django.shortcuts import render
from django.views.generic import FormView
from django.contrib.auth.views import LoginView,TemplateView,LogoutView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,authenticate,logout
from django.http import JsonResponse,HttpResponse,HttpResponseRedirect
from django.urls import reverse_lazy
from business.models import Business
from users.models import CustomUser
# from users.models import Employee
class IndexView(TemplateView):
    template_name="home.html"
class Login(FormView):
    template_name = 'login.html'
    form_class=AuthenticationForm
    success_url=reverse_lazy("base:home")
    def dispatch(self,request,*args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.success_url)
        return super().dispatch(request, *args, **kwargs)
    def post(self,request,*args,**kwargs):
        username=self.request.POST["username"]
        password=self.request.POST["password"]
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_superuser:
                login(self.request,user)
                return JsonResponse({"status":200,"success":self.success_url} ,safe=False)

            else:    
                permission=CustomUser.objects.filter(business__id=request.POST["business"])
                if permission.exists():

                    login(self.request,user)
                    return JsonResponse({"status":200,"success":self.success_url} ,safe=False)

                else:
                    return JsonResponse({"status":500,"message":"No tiene accessos a esta empresa."} ,safe=False)

        return JsonResponse({"status":500,"message":"Usuario o contraseña incorrectos."},safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["business"] = Business.objects.all()
        return context
    
class Logout(LogoutView):
    next_page="/"
