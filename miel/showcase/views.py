from django.db.models import Model
from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import PersonalInfo, CandidateCard
from .serializers import PersonalInfoSerializer


# class CardCandidateAPIView(generics.ListAPIView):
#     queryset = PersonalInfo.objects.all()
#     serializer_class = PersonalInfoSerializer


class PersonaInfoAPIView(APIView):
    def get(self, request):
        c = PersonalInfo.objects.all()   # .values()
        return Response({'cards': PersonalInfoSerializer(c, many=True).data})

    def post(self, request):
        post_new = PersonalInfo.objects.create(
            first_name=request.data['first_name'],
            last_name=request.data['last_name'],
            middle_name=request.data['middle_name'],
            email=request.data['email'],
            city=request.data['city'],
            date_of_birth=request.data['date_of_birth'],
            phone=request.data['phone']


        )
        # return Response({'post': model_to_dict(post_new)})
        return Response({'post': PersonalInfoSerializer(post_new).data})
