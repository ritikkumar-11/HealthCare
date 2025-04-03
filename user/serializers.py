from django.contrib.auth.models import User
from rest_framework import serializers

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True) # so that it only used in POST not in get

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        user = User.objects.create_user( # because it automaticallly hashed the passowrd
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user
