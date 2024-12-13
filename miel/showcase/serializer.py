from rest_framework import serializers
from .models import CandidateCard, Status, Office


# Проверяет наличие статуса и сколько карточек к нему привязаны
class CandidateStatusSerializer(serializers.Serializer):
    status_id = serializers.IntegerField()
    count = serializers.IntegerField()

    def validate_status_id(self, pk):
        if not Status.objects.filter(id=pk).exists():
            raise serializers.ValidationError('Ошибка. Статуса не существует.')
        return pk


# Сколько офисов требуют квоту
class OfficeQuotaSerializer(serializers.Serializer):
    class Meta:
        model = Office
        fields = ['id', 'name', 'quota']

    def get_queryset_not_zero(self):
        return Office.objects.filter(quota__need__gt=0).count()


# Всего кандидатов в базе
class CandidateAllSerializer(serializers.Serializer):
    count = serializers.IntegerField()


# Всего офисов в базе
class OfficeAllSerializer(serializers.Serializer):
    count = serializers.IntegerField()

