from django.shortcuts import render,redirect
from organization.models import Applicants
from django.shortcuts import get_object_or_404

# Create your views here.
# applicants_marketing_approved =  models.BooleanField(default=False)
#     applicants_security_approved =  models.BooleanField(default=False)
#     applicants_kaps_issue =  models.BooleanField(default=False)
def index(request):
    applicants  = Applicants.objects.all()
    pending =  Applicants.objects.filter(applicants_marketing_approved = False,applicants_security_approved =False,applicants_kaps_issue = False).count()
    marketing_approved =  Applicants.objects.filter(applicants_marketing_approved = True,applicants_security_approved =False,applicants_kaps_issue = False).count()
    marketing_approved_security =  Applicants.objects.filter(applicants_marketing_approved = True,applicants_security_approved =True,applicants_kaps_issue = False).count()
    marketing_approved_security_kaps =  Applicants.objects.filter(applicants_marketing_approved = True,applicants_security_approved =True,applicants_kaps_issue = True).count()
    context = {
        'application' : applicants,
        'marketing_approved' : marketing_approved,
        'marketing_approved_security' : marketing_approved_security,
        'marketing_approved_security_kaps' : marketing_approved_security_kaps,
        'pending' : pending



    }
    return render(request,'index_m.html',context)

def new_applicants(request):
    applicants =  Applicants.objects.filter(applicants_marketing_approved = False,applicants_security_approved=False,applicants_kaps_issue=False).order_by("application_send_date")

    context = {
        'application' : applicants
    }
    return render(request,'new_applicants.html',context)


def delete_row(request, slug):
    # article = get_object_or_404(Applicants, slug=slug)
    context = {'slug': slug}
    Applicants.objects.filter(slug = slug).delete()
    
    return redirect("marketing:new_applicants")


