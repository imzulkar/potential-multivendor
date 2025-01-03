# Generated by Django 5.1.4 on 2024-12-29 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("authentications", "0005_rename_is_active_vendorinformation_approval_request"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="vendorinformation",
            name="approval_request",
        ),
        migrations.AddField(
            model_name="vendorinformation",
            name="status",
            field=models.CharField(
                choices=[
                    ("ACTIVE", "Active"),
                    ("DEACTIVATE", "Deactivate"),
                    ("REQUESTED", "Requested"),
                ],
                default="REQUESTED",
                max_length=20,
            ),
        ),
    ]
