from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    Permission,
    PermissionsMixin,
)
from phonenumber_field.modelfields import  PhoneNumberField
from gi_test.helpers.helpers import generate_avatar

from django_acl.models import Group
from .validators import validate_possible_number
from django.utils import timezone
from django.db.models import Q
from django.utils.translation import gettext_lazy as _
from random import randint
from django.utils.text import slugify

def users_image(self, filename):
    return f"assets/users/{filename}"

def user_default_image()             : 
    return f"default/default-image/default-image-for-no-image.png"

class PossiblePhoneNumberField(PhoneNumberField):
    """Less strict field for phone numbers written to database."""

    default_validators = [validate_possible_number]
    
    
    

class UserManager(BaseUserManager):
    def create_user(
        self, email, password=None, is_staff=False, is_active=True, **extra_fields
    ):
        """Create a user instance with the given email and password."""
        email = UserManager.normalize_email(email)
        # Google OAuth2 backend send unnecessary username field
        extra_fields.pop("username", None)

        user = self.model(
            email=email, is_active=is_active, is_staff=is_staff, **extra_fields
        )
        if password:
            user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        return self.create_user(
            email, password, is_staff=True, is_superuser=True, is_admin=True, is_verified=True, **extra_fields
        )

    def customers(self):
        return self.get_queryset().filter(
            Q(is_staff=False) | (Q(is_staff=True) & Q(orders__isnull=False))
        )

    def staff(self):
        return self.get_queryset().filter(is_staff=True)



class User(AbstractBaseUser, PermissionsMixin):
    email                       = models.EmailField(unique=True)
    slug                        = models.SlugField(max_length=256, unique=True, editable=False, blank = True, null = True)
    first_name                  = models.CharField(max_length=256, blank=True)
    last_name                   = models.CharField(max_length=256, blank=True)
    is_staff                    = models.BooleanField(default=False)
    is_active                   = models.BooleanField(default=True)
    note                        = models.TextField(null=True, blank=True)
    date_joined                 = models.DateTimeField(default=timezone.now, editable=False)
    is_verified                 = models.BooleanField(default = True)
    is_admin                    = models.BooleanField(default = False)
    is_logged_in                = models.BooleanField(default = False)
    phone                       = PossiblePhoneNumberField(blank=True, default="")
    image                       = models.FileField(_('Image'), null=True, blank=True, upload_to=users_image, default=user_default_image)

    user_groups = models.ManyToManyField(
        Group,
        verbose_name='groups',
        blank=True,
        related_name='custom_group_set',  # Add or change the related_name here
        related_query_name='custom_group',
    )


    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name='user permissions',
        blank=True,
        related_name='custom_permission_set',  # Add or change the related_name here
        related_query_name='custom_permission',
    )


    USERNAME_FIELD = "email"

    objects = UserManager()

    # slug for User table with releated to first name
    def save(self, *args, **kwargs):
        if not self.slug or self.first_name:
            self.slug = slugify(str(self.first_name))
            if User.objects.filter(slug=self.slug).exclude(pk=self.pk).exists():
                self.slug = slugify(str(self.first_name)) + '-' + str(randint(1, 9999999))
        super(User, self).save(*args, **kwargs)
        
    def __str__(self):
        return str(self.slug)
    
    
    class Meta:
        ordering = ("email",)
        


    

    


