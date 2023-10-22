from rest_framework import serializers
from .models import Person


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person  
        fields = '__all__'
    
    def create(self, validated_data):
        return Person(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.date_of_birth = validated_data.get('date_of_birth', instance.date_of_birth)
        instance.city = validated_data.get('city', instance.city)
        # instance.id_number = validated_data.get('id_number', instance.id_number)
        instance.save()
        return instance
