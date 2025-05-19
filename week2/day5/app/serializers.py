from rest_framework import serializers
from .models import MenuItems, TheUser
from .models import Role

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItems
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = TheUser
        fields = ['username', 'password', 'email', 'role']

    def create(self, validated_data):
        role = validated_data.get('role', Role.USER)
        user = TheUser.objects.create(
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data.get('email', ''),
            role = role
        )
        return user