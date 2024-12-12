import io

from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from .models import PersonalInfo, Office, Status, Experience, Course, CandidateCourse, Skill, CandidateSkill, \
    CandidateCard

# class CandidateCardModel:
#     def __init__(self, first_name, last_name):
#         self.first_name = first_name
#         self.last_name = last_name


# class PersonalInfoSerializer(serializers.Serializer):
#     first_name = serializers.CharField(max_length=255)
#     last_name = serializers.CharField()


User = get_user_model()


class OfficeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Office
        fields = "__all__"


class InvitationToOfficeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Office
        fields = ('name',)


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = ('name',)


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
    gender = serializers.ChoiceField(PersonalInfo.Genders, source='get_gender_display')
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


class WritableNestedModelSerializer:
    pass


class CandidateCardSerializer(WritableNestedModelSerializer):  # TODO
    invitation_to_office = InvitationToOfficeSerializer(allow_null=True, many=True, required=False)
    status = StatusSerializer()
    experience = ExperienceSerializer(many=True, required=False)
    personal_info = PersonalInfoSerializer()
    course = CourseSerializer(read_only=True, source='course_set', required=False)
    skills = SkillSerializer(read_only=True, source='skills_set', required=False)
    comment = serializers.CharField(allow_null=True, required=False)

    class Meta:
        model = CandidateCard
        fields = '__all__'

    def create(self, validated_data):
        return super().create(validated_data)
