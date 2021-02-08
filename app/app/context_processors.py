from business.models import Business
from users.models import CustomUser
def business(request):
        if  request.user.is_authenticated:
            # business=Business.objects.filter(customuser__id=request.user.id)
            user=CustomUser.objects.get(id=request.user.id)
            
            return {"business":user.business.all()}
        else:
            return {"aea":""}
