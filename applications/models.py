from django.db import models

# Create your models here.
from django.conf import settings


class JobApplication(models.Model):

    STATUS_CHOICES = [
        ("Applied", "Applied"),
        ("Screening", "Screening"),
        ("Technical Interview", "Technical Interview"),
        ("HR Interview", "HR Interview"),
        ("Selected", "Selected"),
        ("Rejected", "Rejected"),
    ]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="applications"
    )

    company = models.CharField(max_length=100)

    position = models.CharField(max_length=100)

    location = models.CharField(max_length=100)

    salary = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True
    )

    description = models.TextField(blank=True)

    resume = models.FileField(
        upload_to="resumes/",
        blank=True,
        null=True
    )

    status = models.CharField(
        max_length=30,
        choices=STATUS_CHOICES,
        default="Applied"
    )

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.company} - {self.position}"