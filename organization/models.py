from django.db import models
from accounts.models import ExtraDetails
# Create your models here.
from accounts.models import CustomUser
from django.db.models.signals import pre_save
from django.shortcuts import reverse
from config.utils import unique_slug_generator
#this provides an organization 
class Applicants(models.Model):

    PENDING = "PD"
    APPROVED = "AP"
    REJECTED = "RJ"
    APPLICATION_CHOICES =  [
         (PENDING, 'pending'),
        (APPROVED, 'approved'),
        (REJECTED, 'rejected'),

    ]
    organization =  models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    applicants_name = models.CharField(max_length=255)
    applicants_id_number  =  models.IntegerField()
    applicants_tag_number =  models.CharField(max_length=255)
    applicants_phone_number =  models.CharField(max_length=255)
    applicants_email =  models.EmailField()
    #todo : the departments need to be a list which needs to be provided for so that we enter the lists as categories of department
    applicants_department = models.CharField(max_length=255)
    applicants_vehicle_type =  models.CharField(max_length=255)
    applicants_car_reg_number = models.CharField(max_length=255)
    applicants_log_book_number =  models.CharField(max_length=255)
    #this shows the current duration when the pass needs to be visible
    aplicants_duration =  models.CharField(max_length=255)
    aplicants_status =  models.CharField(max_length=2,choices=APPLICATION_CHOICES,default=PENDING)
    #check if the date when the application was send
    application_send_date =  models.DateTimeField(auto_now=True)
    #check to see the application status
    #this shows if the application is active or not or if it needs renewals
    application_active = models.BooleanField(default=True)
    #marketing approved 
    applicants_marketing_approved =  models.BooleanField(default=False)
    applicants_security_approved =  models.BooleanField(default=False)
    applicants_kaps_issue =  models.BooleanField(default=False)
    slug = models.SlugField(blank=True,unique=True)



    def get_absolute_url(self):
        return reverse("marketing:delete_applicants", kwargs={
            'slug': self.slug
        })
    def __str__(self):
        return self.applicants_email

def product_presave_reciver(sender, instance, *args,**kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(product_presave_reciver,sender = Applicants)
    
    



    
