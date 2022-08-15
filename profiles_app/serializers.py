from rest_framework import serializers
from profiles_app.models import UserProfile,ProfileFeedItem

class Helloserializer(serializers.Serializer):
    """Serializes a name field for testing our APIview"""
    name=serializers.CharField(max_length=10)

class UserProfileSerializer(serializers.ModelSerializer):
    """It is a serializer for User"""

    class Meta:
        model=UserProfile
        fields=['id','name','email','password']
        extra_kwargs={
            'password':{
                'write_only':True,
                'style':{'input_type':'password'}
            }
        }
    
    def create(self,validated_data):
        """Create and return a new user"""
        user=UserProfile.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password']
        )
        return user

class ProfileFeedSerializer(serializers.ModelSerializer):
    class Meta:
        model=ProfileFeedItem
        fields=('id','user_profile','status_txt','created_on')
        extra_kwargs={'user_profile':{'read_only':True}}
        


    

        



