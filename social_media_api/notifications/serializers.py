from rest_framework import serializers
from .models import Notification

class NotificationSerializer(serializers.ModelSerializer):
    actor = serializers.StringRelatedField()
    recipient = serializers.StringRelatedField()
    target = serializers.StringRelatedField()
    class Meta:
        model = Notification
        fields = ['recipient', 'verb', 'target_content_type', 'target_object_id', 'target', 'timestamp']