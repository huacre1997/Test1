from django.forms import *
from .models import CustomUser
from business.models import Business
from datetime import datetime

class CustomMMCF(ModelMultipleChoiceField):
    def label_from_instance(self, member):
        return member.name
class UserForm(ModelForm):
    first_name = CharField(max_length=100, required=True)
    last_name = CharField(max_length=100, required=True)
    business = ModelMultipleChoiceField(
        queryset=Business.objects.all(),
        widget=CheckboxSelectMultiple
    )
    class Meta:
        model = CustomUser
        exclude = ["groups", "user_permissions", "last_login", "date_joined"]
        widgets = {
            'email': EmailInput(attrs={
                "name": "email",
                "id": "email",
                "placeholder": "Ingrese un correo electrónico",
                'class': 'form-control',
            }),
            'password': PasswordInput(render_value=True, attrs={
                "name": "password",
                "id": "password",
                "placeholder": "Contraseña",
                'class': 'form-control',
            })
            


        }



    def save(self, commit=True):
        data = {}
        form = super()
        
        try:
            
            if form.is_valid():
                print("form is valid")
                passwd=self.cleaned_data["password"]
                u = form.save(commit=False)
                if u.pk is None:
                    u.set_password(passwd)
                else:
                    user = CustomUser.objects.get(pk=u.pk) 
                    if user.password != passwd:
                       u.set_password(passwd)
                u.save()
                self.save_m2m()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data