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

    def get_queryset(self):
        pk = self.kwargs.get('pk')

        if not pk:
            return PersonalInfo.objects.all()[:2]

        return PersonalInfo.objects.filter(pk=pk)

    @action(methods=['get'], detail=True)
    def candidate_office(self, request, pk=None):
        office_cand = Office.objects.get(pk=pk)
        return Response({'office_cand': [office_cand.name]})

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


