from django.db import models
from core.utilities.resources import otp_generator
from core.models.abstract import BaseModel
from django.core.exceptions import PermissionDenied


class Profile(BaseModel):
    user = models.OneToOneField("auth.User",on_delete=models.CASCADE,error_messages={"unique":"User already assigned to another profile."})
    otp = models.CharField(max_length=10,default=otp_generator)
    
    class Meta:
        verbose_name_plural = "Account Profile"
        ordering = ["-created_at"]
    
    def regenerate_otp(self):
        self.otp = otp_generator()
        self.save()
    
    def has_request_permission(self,sender_request):
        return any([sender_request.user.is_staff,self.user == sender_request.user])

        
        
            