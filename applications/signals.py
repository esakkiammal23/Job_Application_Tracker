from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import JobApplication


@receiver(post_save, sender=JobApplication)
def application_status_changed(sender, instance, created, **kwargs):

    print("Signal is running...")

    subject = "Job Application Update"

    if created:
        message = (
            f"Hello {instance.user.username},\n\n"
            f"Your application for {instance.company} has been submitted successfully."
        )
    else:
        message = (
            f"Hello {instance.user.username},\n\n"
            f"Your application status has been updated."
        )

    print("About to send email...")
    print("Recipient:", instance.user.email)

    send_mail(
        subject=subject,
        message=message,
        from_email=None,
        recipient_list=[instance.user.email],
        fail_silently=False,
    )

    print("Email function finished.")