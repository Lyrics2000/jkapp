from django.contrib.auth import authenticate, get_user_model, login
from django.shortcuts import render,redirect
from organization.models import Applicants
from .models import CustomUser,ExtraDetails

# Create your views here.

def login(request):
    if request.POST:
        email = request.POST.get('emailAddress')
        password =  request.POST.get('loginPassword')
        user = CustomUser(email = email, password = password)
        if user is not None:
            objectsss = Applicants.objects.all()
            get_email =  ExtraDetails.objects.all()
            for m in get_email:
                if str(m.user) ==  str(user):
                    if str(m.department)  == 'AP':
                        request.session["account_user"] =  str(user)
                        return redirect('organization:index')
                    elif str(m.department)  == 'MT':
                        request.session["account_user"] =  str(user)
                        return redirect('marketing:index')
                    elif str(m.department)  == 'ST':
                        request.session["account_user"] =  str(user)
                        return redirect('security:index')
            context = {
                "applicants" : objectsss
            }
            
    
                   

                
    return render(request,'organization/signin.html',{})
