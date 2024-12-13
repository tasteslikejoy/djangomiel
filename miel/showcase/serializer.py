from rest_framework import serializers
from .models import CandidateCard, Status, Office


# Проверяет наличие статуса и сколько карточек к нему привязаны
class CandidateStatusSerializer(serializers.ModelSerializer):
    candidate_card_count = serializers.SerializerMethodField()

    class Meta:
        model = Status
        fields = ['id', 'name', 'candidate_card_count']

    def get_candidate_card_count(self, obj):
        return CandidateCard.objects.filter(invitation_to_office__status=obj).count()


# Всего кандидатов в базе
class CandidateAllSerializer(serializers.ModelSerializer):
    count = serializers.IntegerField()


# Всего офисов в базе
class OfficeAllSerializer(serializers.ModelSerializer):
    class Meta:
        model = Office
        fields = ['id', 'name', 'location', 'link_to_admin', 'superviser', 'quota']

    def get_queryset_not_zero(self):
        return Office.objects.filter(quota__need__gt=0).count()

