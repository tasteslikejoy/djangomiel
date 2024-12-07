import io

from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from .models import PersonalInfo, CandidateCard


# class CandidateCardModel:
#     def __init__(self, first_name, last_name):
#         self.first_name = first_name
#         self.last_name = last_name


# class PersonalInfoSerializer(serializers.Serializer):
#     first_name = serializers.CharField(max_length=255)
#     last_name = serializers.CharField()

class PersonalInfoSerializer(serializers.Serializer):
    email = serializers.EmailField()
    phone = serializers.CharField(max_length=30 )
    contact_link = serializers.CharField(max_length=255, read_only=True)
    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)
    middle_name = serializers.CharField(max_length=50)
    city = serializers.CharField(max_length=50)
    gender = serializers.CharField(read_only=True)
    date_of_birth = serializers.DateTimeField()

    def create(self, validated_data):
        return PersonalInfo.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.contact_link = validated_data.get('contact_link', instance.contact_link)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.middle_name = validated_data.get('middle_name', instance.middle_name)
        instance.city = validated_data.get('city', instance.city)
        instance.gender = validated_data.get('gender', instance.gender)
        instance.date_of_birth = validated_data.get('date_of_birth', instance.date_of_birth)
        instance.save()
        return instance

# def encode():
#     model = CandidateCardModel('Semen', 'Firsov')
#     model_sr = PersonalInfoSerializer(model)
#     print(model_sr.data, type(model_sr.data), sep='\n')
#     json = JSONRenderer().render(model_sr.data)
#     print(json)
#
#
# def decode():
#     stream = io.BytesIO(b'{"first_name":"Semen","last_name":"Firsov"}')
#     data = JSONParser().parse(stream)
#     serializer = PersonalInfoSerializer(data=data)
#     serializer.is_valid()
#     print(serializer.validated_data)
