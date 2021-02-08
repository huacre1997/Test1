from django.forms import *
from .models import Business
from datetime import datetime
class BusinessForm(ModelForm):
   
   
    class Meta:
        model = Business
        fields=["name","ruc","status"]
        exclude = ["created", "updated"]
     

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                "class": "form-control",
            })
       
    
    

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data
    def clean_ruc(self):
        ruc=self.cleaned_data["ruc"]
        ap=Business.objects.filter(ruc__iexact=ruc)

        if self.instance  :
            ap = ap.exclude(pk=self.instance.pk)

        if ap:
            raise forms.ValidationError("El ruc "+ruc+" ya está registrado.")
        return ruc
    def clean_name(self):
            name=self.cleaned_data["name"]
            ap=Business.objects.filter(name__iexact=name)

            if self.instance  :
                ap = ap.exclude(pk=self.instance.pk)

            if ap:
                raise forms.ValidationError("La razon social '"+name+"' ya está registrada.")
            return name
