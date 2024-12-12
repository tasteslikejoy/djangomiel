from rest_framework import serializers

from showcase.models import CandidateCard


class CandidateCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = CandidateCard
        fields = ['id','created_at','current_workplace','current_occupation','employment_date',
                  'comment','favorite','archived','synopsis','objects_card','clients_card',
                  'invitation_to_office','experience','personal_info']
        extra_kwargs = {
            'id': {'read_only': True},
            'created_at': {'read_only': True},
        }


class CandidateCardSerializerDirektor(serializers.ModelSerializer):
    class Meta:
        model = CandidateCard
        fields = ['id','created_at','current_workplace','current_occupation','employment_date',
                  'comment','favorite','invitation_to_office','experience']
        extra_kwargs = {
            'id': {'read_only': True},
            'created_at': {'read_only': True},
        }

