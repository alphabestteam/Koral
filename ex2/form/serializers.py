from rest_framework import serializers
from .models import Form, FileSharingForm, MessagesForm



class FormSerializer(serializers.ModelSerializer):
    class Meta:
        model = Form
        fields = "__all__"

    def update(self, instance, validated_data):
        instance.open_date = validated_data.get('open_date', instance.open_date)
        instance.close_date = validated_data.get('close_date', instance.close_date)
        instance.event_reporter = validated_data.get('event_reporter', instance.event_reporter)
        instance.event_status = validated_data.get('event_status', instance.event_status)
        instance.ability_open_a_draft = validated_data.get('ability_open_a_draft', instance.ability_open_a_draft)
        instance.ability_download_form_archive = validated_data.get('ability_download_form_archive', instance.ability_download_form_archive)
        instance.shared_users = validated_data.get('shared_users', instance.shared_users)
        instance.save()
        return instance
    
class FileSharingFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileSharingForm
        fields = "__all__"


class MessagesFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = MessagesForm
        fields = "__all__"

    

