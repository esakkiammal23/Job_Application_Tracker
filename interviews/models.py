from django.db import models

# Create your models here.
from django.db import models
from applications.models import JobApplication


class InterviewRound(models.Model):

    RESULT_CHOICES = [
        ("Pending", "Pending"),
        ("Passed", "Passed"),
        ("Failed", "Failed"),
    ]

    application = models.ForeignKey(
        JobApplication,
        on_delete=models.CASCADE,
        related_name="interview_rounds"
    )

    round_name = models.CharField(max_length=100)

    interview_date = models.DateField()

    interviewer = models.CharField(
        max_length=100,
        blank=True
    )

    feedback = models.TextField(
        blank=True
    )

    result = models.CharField(
        max_length=20,
        choices=RESULT_CHOICES,
        default="Pending"
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.application.company} - {self.round_name}"