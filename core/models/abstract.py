from typing import Iterable, Optional
from django.db import models
from core.utilities.resources import timesince

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    created_by = models.ForeignKey("auth.User",models.SET_NULL,related_name="creator",null=True,blank=True)
    modified_by = models.ForeignKey("auth.User",models.SET_NULL,related_name="modifier",null=True,blank=True)
    
    def created_since(self):
        return timesince(self.created_at)
    
    def updated_since(self):
        return timesince(self.updated_at)
    
    class Meta:
        abstract = True
    