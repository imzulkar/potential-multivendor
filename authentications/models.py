from django.contrib.auth.models import BaseUserManager
from django.db import transaction
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.core.validators import RegexValidator

from core.models import BaseModel
from utils import content_file_path


class UserManager(BaseUserManager):
    @transaction.atomic
    def create_user(
        self, email, password=None,  role=None
    ):

        if not role:
            raise ValueError("Role should not be empty")

        if not email:
            raise ValueError("Email should not be empty")



        if email:
            user = self.model(
                email=self.normalize_email(email=email),
                role=role,
            )
        else:
            user = self.model(role=role)

        user.set_password(password)
        user.save(using=self._db)
        return user

    @transaction.atomic
    def create_superuser(
        self, email, password=None,  role="ADMIN"
    ):
        if not password:
            raise ValueError("Password should not be empty")

        user = self.create_user(
            email=email,
            password=password,
            role=role,
        )
        user.is_superuser = True
        user.is_staff = True
        user.is_active = True
        user.save(using=self._db)
        return user
class User(AbstractBaseUser, PermissionsMixin):


    ROLE = (
        ("ADMIN", "Admin"),
        ("VENDOR", "Vendor"),
        ("CUSTOMER", "Customer"),
    )

    email = models.EmailField(
        max_length=100,
        verbose_name="Email",
        unique=True,
    )
    first_name = models.CharField(max_length=200,null=True, blank=True, verbose_name="First Name")
    last_name = models.CharField(max_length=200, null=True, blank=True,verbose_name="Last Name")
    phone_number = models.CharField(max_length=15, null=True, blank=True, verbose_name="Phone Number", validators=[
            RegexValidator(
                regex=r'^\+?1?\d{9,15}$',  # Example regex for international phone numbers
                message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
            )
        ])
    profile_picture = models.ImageField(
        upload_to=content_file_path,
        null=True,
        blank=True,
        verbose_name="Profile Picture",
    )
    role = models.CharField(choices=ROLE, max_length=10, default="CUSTOMER")
    date_joined = models.DateTimeField(
        verbose_name="Date Joined",
        auto_now_add=True,
    )
    last_login = models.DateTimeField(auto_now=True)

    # user role
    is_superuser = models.BooleanField(
        verbose_name="Superuser Status",
        default=False,
        help_text="Designate if the " "user has superuser " "status",
    )
    is_staff = models.BooleanField(
        verbose_name="Staff Status",
        default=False,
        help_text="Designate if the user has " "staff status",
    )
    is_active = models.BooleanField(
        verbose_name="Active Status",
        default=True,
        help_text="Designate if the user has " "active status",
    )

    USERNAME_FIELD = "email"
    objects = UserManager()

    def __str__(self):
        return self.email

    class Meta:
        ordering = ["-date_joined"]


class VendorInformation(BaseModel):
    """
    Vendor Information Model
    """

    user = models.OneToOneField(
        "User",
        on_delete=models.CASCADE,
        related_name="vendor_information",
        verbose_name="User",
    )
    business_name = models.CharField(
        max_length=255, null=False, blank=False, verbose_name="Business Name"
    )
    business_email = models.EmailField(
        max_length=255, null=False, blank=False, verbose_name="Business Email"
    )
    address = models.TextField(
        null=True, blank=True, verbose_name="Business Address"
    )

    phone_number = models.CharField(
        max_length=15,
        null=True,
        blank=True,
        verbose_name="Contact Number",
        validators=[
            RegexValidator(
                regex=r"^\+?1?\d{9,15}$",
                message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.",
            )
        ],
    )

    def __str__(self):
        return self.business_name

    class Meta:
        verbose_name = "Vendor Information"
        verbose_name_plural = "Vendors Information"
    