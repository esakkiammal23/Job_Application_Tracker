from rest_framework import serializers
from .models import InterviewRound


class InterviewRoundSerializer(serializers.ModelSerializer):

    class Meta:
        model = InterviewRound
        fields = "__all__"
        read_only_fields = ["created_at"]