from django.shortcuts import render,redirect
import pandas as pd
from .models import  Applicants
from accounts.models import CustomUser
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView,View,ListView
from django.shortcuts import get_object_or_404

# Create your views here.
def index(request):
    applicants  = Applicants.objects.all()
    context = {
        'application' : applicants
    }
    return render(request,'index.html',context)


def file_upload(request):
    if request.method ==  "POST":
        uploaded_files =  request.FILES["excel_file"]
        upload_name =  uploaded_files.name
        df = pd.read_excel (uploaded_files)
        accounts_name = request.session.get("account_user")
        user =  CustomUser.objects.get(email=accounts_name)
        applicants  = Applicants.objects.all()
        for index, row in df.iterrows():
            app = Applicants(
                organization = user,
                applicants_name=row["Applicant_Name"],
                applicants_id_number = row["Applicant_ID"],
                applicants_tag_number = row["Applicant_Tag_NO"],
                applicants_phone_number = row["Applicant_Phone_Number"],
                applicants_email = row["Applicant_Email"],
                applicants_department = row["Applicant_Department"],
                applicants_vehicle_type = row["Applicant_Vehicle_Type"],
                applicants_car_reg_number = row["Applicant_Car_Reg_NO"],
                applicants_log_book_number = row["Applicant_Log_Book_NO"],
                aplicants_duration = row["Applicant_Duration"]
                
            )
            app.save()
           
    context = {
        'application' : applicants
    }
    return render(request,'index.html',context)



