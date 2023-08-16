from rest_framework.viewsets import ModelViewSet
from core.models.profiles import Profile
from core.serializers.profile import UserSerializer,ProfileSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from rest_framework import status
from core.tasks.email import send_otp_email

class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
class ProfileViewSet(ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    
    @action(detail=True, methods=['get','post'], permission_classes=[IsAuthenticated])
    def send_otpcode(self, request, pk=None):
        profile = self.get_object()
        profile.regenerate_otp()
        otp_code = profile.otp
        email = profile.user.email if profile.user.email else ...
        print([profile,otp_code])
        if email:
            send_otp_email.delay(email,otp_code) if email else ...
            return Response(data=[{'status': "We have sent otp code to your email"}],status=status.HTTP_200_OK)
        else:
            return Response(data=[{'status': "We have sent otp code to your email"}],status=status.HTTP_200_OK)
            