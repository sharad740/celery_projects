from time import sleep
from django.core.mail import send_mail
from celery import shared_task

@shared_task()
def send_feedback_email_task(email_address, message):
    """Sends an email when the feedback form has been submitted."""
    send_mail(
        subject="Your Feedback",
        message=f"\t{message}\n\nThank you!",
        from_email="noreply@successbusiness.com",
        recipient_list=[email_address],
        fail_silently=False,
    )
    
@shared_task()
def send_otp_email(email_address,otp_code):
    """Sends an email when the feedback form has been submitted."""
    return send_mail(
        subject="Confirm your Account",
        message=f"Your otp code is {otp_code}.Please do not share this to anyone.\nThank you!",
        from_email="noreply@successbusiness.com",
        recipient_list=[email_address],
        fail_silently=True,
    )
    