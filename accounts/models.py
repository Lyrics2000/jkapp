from django.db import models

# src/users/model.py
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractUser




class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """
    def create_user(self, email, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError(_('The Email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, **extra_fields)


# src/users/model.py


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)
    

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email




#creates a model to hold extra fields of registration
class ExtraDetails(models.Model):
    APPLICATION = 'AP'
    MARKETING = 'MT'
    SECURITY = 'ST'
    KAPS = 'PK'
    DEPARTMENT_CHOICES = [
        (APPLICATION, 'Application'),
        (MARKETING, 'Marketing'),
        (SECURITY, 'Security'),
        (KAPS, 'Kaps'),

    ]


    #organizations 
    RESIDENTIAL = 'RS'
    NONRESIDENTIAL = 'NR'
    RESIDENTIAL_NONRESIDENTIAL_CHOICES = [
        (RESIDENTIAL, 'Residential'),
        (NONRESIDENTIAL, 'Non Residential'),

    ]

    #governmental non governmenta
    GOVERNMENTAL = 'GR'
    NONGOVERNMENTAL = 'NG'
    GOVERNMENTAL_NONGOVERNMENTAL_CHOICES = [
        (GOVERNMENTAL, 'Governmental'),
        (NONGOVERNMENTAL, 'Non Governmental'),

    ]
    ORGANIZATION_CHOICES = [
    ('RESIDENTIAL_GOVERNMENTAL', (
            ('vinyl', 'Vinyl'),
            ('cd', 'CD'),
        )
    ),
    ('RESIDENTIAL_NON_GOVERNMENTAL', (
            ('vhs', 'VHS ape'),
            ('dvd', 'DVD'),
        )
    ),

    ('NON_RESIDENTIAL_NON_GOVERNMENTAL', (
            ('vhs', 'VHS Tape'),
            ('dvd', 'DVD'),
        )
    ),
    ('NON_RESIDENTIAL_GOVERNMENTAL', (
            ('vhs', 'VHS Tape'),
            ('dvd', 'DVD'),
        )
    ),

    
]
    user =  models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    first_name =  models.CharField(max_length=255)
    last_name =  models.CharField(max_length=255)
    id_number = models.IntegerField()
    tag_number = models.CharField(max_length=255)
    department =  models.CharField(max_length=2,choices=DEPARTMENT_CHOICES,default=APPLICATION)
    residential_non_residential_organization = models.CharField(max_length=2,choices=RESIDENTIAL_NONRESIDENTIAL_CHOICES,default=RESIDENTIAL)
    governmental_non_govermental = models.CharField(max_length=2,choices=GOVERNMENTAL_NONGOVERNMENTAL_CHOICES,default=GOVERNMENTAL)
    organization = models.CharField(max_length=255,choices=ORGANIZATION_CHOICES,default=APPLICATION)
    
    def __str__(self):
        return str(self.tag_number)
        
    
    


