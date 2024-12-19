from django.contrib.auth import get_user_model
from rest_framework import serializers
from drf_writable_nested import WritableNestedModelSerializer
from rest_framework.exceptions import ValidationError

from .models import (CandidateCard, Office, Status, Experience, PersonalInfo, Course, Skill,
                     CandidateCourse, CandidateSkill, Quota, Invitations)

User = get_user_model()


#
# class InvitationToOfficeSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Office
#         fields = ('status',)


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = ('name',)


# class InvitationToOfficeSerializer(WritableNestedModelSerializer):
#     status = StatusSerializer(required=False)
#
#     class Meta:
#         model = Invitations
#         fields = ('status',)


class ExperienceSerializer(serializers.ModelSerializer):
    date_start = serializers.DateTimeField(format='%d.%m.%Y %H:%M:%S')
    date_end = serializers.DateTimeField(format='%d.%m.%Y %H:%M:%S')

    class Meta:
        model = Experience
        fields = (
            'workplace',
            'occupation',
            'date_start',
            'date_end',
        )


class PersonalInfoSerializer(serializers.ModelSerializer):
    gender = serializers.ChoiceField(PersonalInfo.Genders)  # TODO чекнуть
    email = serializers.EmailField()
    contact_link = serializers.CharField(allow_blank=True, required=False)

    class Meta:
        model = PersonalInfo
        fields = (
            'email',
            'phone',
            'contact_link',
            'first_name',
            'last_name',
            'middle_name',
            'city',
            'gender',
            'date_of_birth',
        )


class CourseSerializer(serializers.ModelSerializer):
    progress = serializers.IntegerField()

    class Meta:
        model = Course
        has_through_model = CandidateCourse
        fields = (
            'name',
            'progress',
        )


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        has_through_model = CandidateSkill
        fields = ('name',)


class CandidateCardSerializer(WritableNestedModelSerializer):  # TODO
    # invitation_to_office = InvitationToOfficeSerializer(allow_null=True, many=True, required=False)
    experience = ExperienceSerializer(many=True, required=False)
    personal_info = PersonalInfoSerializer()
    course = CourseSerializer(read_only=True, source='course_set', required=False)
    skills = SkillSerializer(read_only=True, source='skills_set', required=False)
    comment = serializers.CharField(allow_null=True, required=False)

    class Meta:
        model = CandidateCard
        fields = ['created_at', 'current_workplace', 'current_occupation',
                  'employment_date', 'comment', 'archived', 'synopsis',
                  'objects_card', 'clients_card', 'experience', 'personal_info',
                  'course', 'skills']
        read_only_fields = ('id',)


# Alice


# Проверяет наличие статуса и сколько карточек к нему привязаны
class CandidateStatusSerializer(serializers.ModelSerializer):
    candidate_card_count = serializers.SerializerMethodField()

    class Meta:
        model = Status
        fields = ['id', 'name', 'candidate_card_count']

    def get_candidate_card_count(self, obj):
        return CandidateCard.objects.filter(cards__status=obj).count()


# Всего кандидатов в базе
class CandidateAllSerializer(serializers.Serializer):
    count = serializers.IntegerField()


class QuotaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quota
        fields = (
            'quantity',
            'default',
            'used',
            'need',
            'date',
            'office'
        )


class QuotaAutoCreateSerializer(serializers.ModelSerializer):
    quantity = serializers.IntegerField(required=False, default=10)
    default = serializers.IntegerField(required=False, default=10)

    class Meta:
        model = Quota
        fields = (
            'quantity',
            'default',
        )


# Всего офисов в базе
class OfficeAllSerializer(serializers.ModelSerializer):
    quotas = QuotaSerializer(many=True, required=False)
    invitation_count = serializers.SerializerMethodField()
    employed_count = serializers.SerializerMethodField()

    class Meta:
        model = Office
        fields = ['id', 'name', 'location', 'link_to_admin', 'superviser',
                  'quotas', 'invitation_count', 'employed_count']

    def get_queryset_not_zero(self):
        return Office.objects.filter(quotas__need__gt=0).count()

    def get_invitation_count(self, obj):
        return Invitations.objects.filter(office=obj).count()

    def get_employed_count(self, obj):
        try:
            accepted_status = Status.objects.get(name='Принят в штат')
            return CandidateCard.objects.filter(
                cards__office=obj,
                cards__status__in=[accepted_status.id]
            ).count()
        except Status.DoesNotExist:
            return 0

    def create(self, validated_data):
        quotas_data = validated_data.pop('quotas', None)
        office = Office.objects.create(**validated_data)

        if quotas_data:
            for quota_data in quotas_data:
                Quota.objects.create(office=office, **quota_data)
        else:
            quotas_default = {
                'quantity': validated_data.get('quantity', 10),
                'default': validated_data.get('default', 10),
                'need': validated_data.get('need', 10)
            }
            Quota.objects.create(office=office, **quotas_default)
        return office

    def update(self, instance, validated_data):
        quotas_data = validated_data.pop('quotas', None)

        instance.name = validated_data.get('name', instance.name)
        instance.location = validated_data.get('location', instance.location)
        instance.link_to_admin = validated_data.get('link_to_admin', instance.link_to_admin)
        instance.superviser = validated_data.get('superviser', instance.superviser)

        if quotas_data is not None:
            instance.quotas.all().delete()
            for quota_data in quotas_data:
                Quota.objects.create(office=instance, **quota_data)

        instance.save()
        return instance


class InvitationSerializer(WritableNestedModelSerializer):
    office = OfficeAllSerializer(required=False)
    status = StatusSerializer(required=False)

    class Meta:
        model = Invitations
        fields = ['office', 'status', 'candidate_card']


class CoursesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['name']


# Валерааааааа

class AdminShowcaseSerializer(serializers.ModelSerializer):
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
        fields = ['id', 'created_at', 'current_workplace', 'current_occupation', 'employment_date',
                  'comment', 'archived', 'synopsis', 'objects_card', 'clients_card',
                  'experience', 'personal_info',
                  'email', 'phone', 'contact_link',
                  'first_name', 'last_name', 'middle_name', 'city', 'gender', 'date_of_birth']
        extra_kwargs = {
            'id': {'read_only': True},
            'created_at': {'read_only': True},
        }


class SuperviserShowcaseSerializer(serializers.ModelSerializer):
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
        fields = ['id', 'created_at', 'current_workplace', 'current_occupation', 'email', 'phone', 'contact_link',
                  'first_name', 'last_name', 'middle_name', 'city', 'gender', 'date_of_birth']
        extra_kwargs = {
            'id': {'read_only': True},
            'created_at': {'read_only': True},
        }
