from django import forms
from core.tasks.email import send_feedback_email_task

class FeedbackForm(forms.Form):
    email = forms.EmailField(label="Email Address")
    message = forms.CharField(
        label="Message", widget=forms.Textarea(attrs={"rows": 5})
    )

    def send_email(self):
        email = self.cleaned_data["email"]
        message = self.cleaned_data["message"]
        
        send_feedback_email_task.delay(email, message)
    