from django.shortcuts import render
from django.template.loader import render_to_string
from django.contrib.auth import authenticate
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.http import JsonResponse,HttpResponse,HttpResponseRedirect
import json
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.models import User
from .models import CustomUser
from django.forms.models import model_to_dict
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.http import HttpResponse
from .forms import UserForm

class EmployeeListView(generic.ListView,LoginRequiredMixin):
    model=User
    
    template_name="user_list.html"
    login_url = "bases:login"
    @method_decorator(csrf_exempt)
    def dispatch(self,request,*args, **kwargs):
        return super().dispatch(request,*args,**kwargs)
    
    def post(self,request,*args, **kwargs):
        data={}
        try:
            action=request.POST["action"]
            if action=="searchData":
                data=[]
                for i in CustomUser.objects.all():
                    data.append(i.toJSON())   
            else:
                data["error"]="Ha ocurrido un error aea"
        except Exception as e:
            print(e)
        return JsonResponse(data,safe=False)
class CreateUserView(LoginRequiredMixin,generic.CreateView):
    model = User
    form_class = UserForm
    login_url = "base:login"
    template_name="user_form.html"
    def post(self,request,*args, **kwargs):
        data={}
        try:
            action=request.POST["action"]
            if action=="add":
                form = self.get_form()
                if form.is_valid():
                    print("if is valid")

                    form.save()
                    
                   
                    data = {
                    'stat': 'ok',
                   }
                    return JsonResponse(data)

                else:
                    print("not valid")

                    data = {
                    "error":form.errors,
                    'stat': False,
                    }
                    return JsonResponse(data)
            else:
                print("else")
                data["error"]="Nose ha ingresado nadas"
                return HttpResponse("error")
        except Exception as e:
            print(e)
class EditUserView(LoginRequiredMixin, generic.UpdateView):
    model = CustomUser
    template_name="user_form.html"
    context_object_name = "obj" 
    form_class = UserForm
    login_url = "bases:login"

    def dispatch(self,request,*args, **kwargs):
        self.object=self.get_object() 
        return super().dispatch(request,*args,**kwargs)
    def post(self,request,*args, **kwargs):
        data={}
        try:
            action=request.POST["action"]
            print(f'action es {action}')
            print(request.POST)
            if action=="edit":
                form = self.get_form()
    
                if form.is_valid():
                    
                    form.save()
                    data = {
                    'stat': 'ok',
                   }
                    return JsonResponse(data)
                else:
                    data = {
                    "error":form.errors,
                    'stat': False,
                    }
                    return JsonResponse(data)
            else:
                data["error"]="Nose ha ingresado nada"
        except Exception as e:
            print(e)