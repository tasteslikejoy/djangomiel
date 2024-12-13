from rest_framework import serializers
from .models import CandidateCard, Status


class CandidateStatusSerializer(serializers.Serializer):
    status_id = serializers.IntegerField()
    count = serializers.IntegerField()

    def validate_status_id(self, pk):
        if not Status.objects.filter(id=pk).exists():
            raise serializers.ValidationError('Ошибка. Статуса не существует.')
        return pk