from rest_framework import serializers

from showcase.models import CandidateCard



class CandidateCardSerializer(serializers.ModelSerializer):
    email = serializers.CharField(source='personal_info.email', read_only=True)
    phone = serializers.CharField(source='personal_info.phone', read_only=True)
    contact_link = serializers.CharField(source='personal_info.contact_link', read_only=True)
    first_name = serializers.CharField(source='personal_info.first_name', read_only=True)
    last_name = serializers.CharField(source='personal_info.last_name', read_only=True)
    middle_name = serializers.CharField(source='personal_info.middle_name', read_only=True)
    city = serializers.CharField(source='personal_info.city', read_only=True)
    gender = serializers.CharField(source='personal_info.gender', read_only=True)
    date_of_birth = serializers.CharField(source='personal_info.date_of_birth', read_only=True)
    class Meta:
        model = CandidateCard
        fields = ['id','created_at','current_workplace','current_occupation','employment_date',
                  'comment','favorite','archived','synopsis','objects_card','clients_card',
                  'invitation_to_office','experience','personal_info',
                  'email','phone','contact_link',
                  'first_name','last_name','middle_name','city','gender','date_of_birth']
        extra_kwargs = {
            'id': {'read_only': True},
            'created_at': {'read_only': True},
        }


class CandidateCardSerializerDirektor(serializers.ModelSerializer):
    email = serializers.CharField(source='personal_info.email', read_only=True)
    phone = serializers.CharField(source='personal_info.phone', read_only=True)
    contact_link = serializers.CharField(source='personal_info.contact_link', read_only=True)
    first_name = serializers.CharField(source='personal_info.first_name', read_only=True)
    last_name = serializers.CharField(source='personal_info.last_name', read_only=True)
    middle_name = serializers.CharField(source='personal_info.middle_name', read_only=True)
    city = serializers.CharField(source='personal_info.city', read_only=True)
    gender = serializers.CharField(source='personal_info.gender', read_only=True)
    date_of_birth = serializers.CharField(source='personal_info.date_of_birth', read_only=True)

    class Meta:
        model = CandidateCard
        fields = ['id','created_at','current_workplace','current_occupation','email','phone','contact_link',
                  'first_name','last_name','middle_name','city','gender','date_of_birth']
        extra_kwargs = {
            'id': {'read_only': True},
            'created_at': {'read_only': True},
        }

