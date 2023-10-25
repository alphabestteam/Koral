from rest_framework import serializers
from .models import User



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'id_number', 'email', 'unread_messages')

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.username = validated_data.get('username', instance.username)
        instance.id_number = validated_data.get('id_number', instance.id_number)
        instance.email = validated_data.get('email', instance.email)
        instance.unread_messages = validated_data.get('unread_messages', instance.unread_messages)
        instance.save()
        return instance
