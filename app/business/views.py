from django.shortcuts import render
from django.views import generic
from business.models import Business
class BusinessView(generic.ListView):
    template_name = "List_Business.html"
    model=Business
    
class CreateBusinessView(generic.CreateView):
    template_name = "Create_Business.html"
    model=Business