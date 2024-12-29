# Generated by Django 5.1.4 on 2024-12-29 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "email",
                    models.EmailField(
                        max_length=100, unique=True, verbose_name="Email"
                    ),
                ),
                (
                    "role",
                    models.CharField(
                        choices=[
                            ("ADMIN", "Admin"),
                            ("VENDOR", "Vendor"),
                            ("CUSTOMER", "Customer"),
                        ],
                        default="user",
                        max_length=10,
                    ),
                ),
                (
                    "date_joined",
                    models.DateTimeField(auto_now_add=True, verbose_name="Date Joined"),
                ),
                ("last_login", models.DateTimeField(auto_now=True)),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designate if the user has superuser status",
                        verbose_name="Superuser Status",
                    ),
                ),
                (
                    "is_staff",
                    models.BooleanField(
                        default=False,
                        help_text="Designate if the user has staff status",
                        verbose_name="Staff Status",
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(
                        default=True,
                        help_text="Designate if the user has active status",
                        verbose_name="Active Status",
                    ),
                ),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={
                "ordering": ["-date_joined"],
            },
        ),
    ]
