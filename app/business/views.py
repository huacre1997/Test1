from django.shortcuts import render
from django.views import generic
from business.models import Business
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.http import JsonResponse,HttpResponse,HttpResponseRedirect
from .forms import BusinessForm
from django.urls import reverse_lazy

class BusinessView(LoginRequiredMixin,generic.ListView):
    template_name = "list_business.html"
    model=Business
    login_url = "base:login"

    @method_decorator(csrf_exempt)
    def dispatch(self,request,*args, **kwargs):
        return super().dispatch(request,*args,**kwargs)
    def post(self,request,*args, **kwargs):
        data={}
        try:
            action=request.POST["action"]
            if action=="searchData":
                data=[]
                for i in Business.objects.all():
                    data.append(i.toJSON())
            else:
                data["error"]="Ha ocurrido un error"
        except Exception as e:
            print(e)
        return JsonResponse(data,safe=False)


class CreateBusinessView(generic.CreateView):
    template_name = "create_business.html"
    model=Business
    context_object_name = "obj"
    form_class = BusinessForm
    login_url = "bases:login"

    success_url = reverse_lazy("business:create_business")

    def post(self,request,*args, **kwargs):
        data={}
        action=self.request.POST["action"]
        if action=="add":
            form=BusinessForm(self.request.POST)
            if form.is_valid():
                form.save()
                data = {
                'stat': 'ok',
                }
                return JsonResponse(data,safe=False)

            else:
                # data = render_to_string(self.template_name,{'form': form}, request=request)
                data = {
                    "error":form.errors,
                    'stat': False,
                    }
                return JsonResponse(data)
        else:
            data["error"]="Nose ha ingresado nadas"
class EditBusinessView(generic.UpdateView):
    model = Business
    template_name = "create_business.html"
    context_object_name = "obj"
    form_class = BusinessForm
    login_url = "base:login"
    def dispatch(self,request,*args, **kwargs):
        self.object=self.get_object() 
        return super().dispatch(request,*args,**kwargs)
    def post(self,request,*args, **kwargs):
        data={}
        action=request.POST["action"]
        if action=="edit":
            form = self.get_form()
            if form.is_valid():
                form.instance.updatedUsu = self.request.user.id
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
    def form_valid(self, form):
        form.instance.updatedUsu = self.request.user.id
        return super().form_valid(form)


    def producto_inactivar(request, id):
        prod = Business.objects.filter(pk=id).first()
        contexto = {}
        template_name = "inv/catalogo_del.html"
        if not prod:
            redirect("inv:product_list")
        if request.method == "GET":
            contexto = {"obj": prod}
        if request.method == "POST":
            prod.estado = False
            prod.save()
            return redirect("inv:product_list")

        return render(request, template_name, contexto)