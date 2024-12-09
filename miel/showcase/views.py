from django.db.models import Model
from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics, viewsets, mixins
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet

from .models import PersonalInfo, CandidateCard, Office
from .serializers import PersonalInfoSerializer


# class CardCandidateAPIView(generics.ListAPIView):
#     queryset = PersonalInfo.objects.all()
#     serializer_class = PersonalInfoSerializer


class PersonalInfoViewSet(mixins.CreateModelMixin,
                          mixins.RetrieveModelMixin,
                          mixins.UpdateModelMixin,
                          mixins.ListModelMixin,
                          GenericViewSet):
    queryset = PersonalInfo.objects.all()
    serializer_class = PersonalInfoSerializer

    @action(methods=['get'], detail=True)
    def candidate_office(self, request, pk=None):
        office_cand = Office.objects.all()
        return Response({'office_cand': [c.name for c in office_cand]})

# class PersonalInfoAPIList(generics.ListCreateAPIView):
#     queryset = PersonalInfo.objects.all()
#     serializer_class = PersonalInfoSerializer
#
#
# class PersonalInfoAPIUpdate(generics.UpdateAPIView):
#     queryset = PersonalInfo.objects.all()
#     serializer_class = PersonalInfoSerializer
#
#
# class PersonalInfoDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = PersonalInfo.objects.all()
#     serializer_class = PersonalInfoSerializer


