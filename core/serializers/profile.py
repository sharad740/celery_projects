from rest_framework import serializers
from core.models.profiles import Profile
from django.contrib.auth.models import User

class UserSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.HyperlinkedIdentityField(view_name="users-detail")
    
    class Meta:
        model = User
        fields = ['id','username','email','first_name','last_name']   

class ProfileSerializer(serializers.ModelSerializer):
    id = serializers.HyperlinkedIdentityField(view_name="profile-detail")
    user = UserSerializer()
    
    class Meta:
        model = Profile
        fields = ["id","user",'otp']
    