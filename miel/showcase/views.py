from django.db.models import Model
from django.shortcuts import render
from rest_framework import generics

from .models import PersonalInfo
from .serializers import PersonalInfoSerializer


class CardCandidateAPIView(generics.ListAPIView):
    queryset = PersonalInfo.objects.all()
    serializer_class = PersonalInfoSerializer


