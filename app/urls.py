from django.urls import path
from django.views import generic
from core.views.send_feedback import FeedbackFormView,SuccessView

urlpatterns = [
    path('',FeedbackFormView.as_view(),name="form-create"),    
    path('success/',SuccessView.as_view(),name="form-success")    
]
