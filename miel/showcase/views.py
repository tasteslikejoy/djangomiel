from django.db.models import Model
from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics, viewsets, mixins
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet

from .models import PersonalInfo, CandidateCard, Office
from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from .serializers import PersonalInfoSerializer, OfficeSerializer


# class CardCandidateAPIView(generics.ListAPIView):
#     queryset = PersonalInfo.objects.all()
#     serializer_class = PersonalInfoSerializer


# class PersonalInfoViewSet(mixins.CreateModelMixin,
#                           mixins.RetrieveModelMixin,
#                           mixins.UpdateModelMixin,
#                           mixins.ListModelMixin,
#                           GenericViewSet):
#     queryset = PersonalInfo.objects.all()
#     serializer_class = PersonalInfoSerializer
#
#     def get_queryset(self):
#         pk = self.kwargs.get('pk')
#
#         if not pk:
#             return PersonalInfo.objects.all()[:2]
#
#         return PersonalInfo.objects.filter(pk=pk)
#
#     @action(methods=['get'], detail=True)
#     def candidate_office(self, request, pk=None):
#         office_cand = Office.objects.get(pk=pk)
#         return Response({'office_cand': office_cand.name})

# class PersonalInfoAPIListPagination(PageNumberPagination):
#     page_size = 2
#     page_size_query_param = 'page_size'
#     max_page_size = 10000

class PersonalInfoAPIList(generics.ListCreateAPIView):
    queryset = PersonalInfo.objects.all()
    serializer_class = PersonalInfoSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    # pagination_class = PersonalInfoAPIListPagination


class PersonalInfoAPIUpdate(generics.RetrieveUpdateAPIView  ):
    queryset = PersonalInfo.objects.all()
    serializer_class = PersonalInfoSerializer
    permission_classes = (IsAuthenticated,)
    # authentication_classes = (TokenAuthentication,)


class PersonalInfoAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = PersonalInfo.objects.all()
    serializer_class = PersonalInfoSerializer
    permission_classes = (IsAdminOrReadOnly,)


class OfficeListAPI(generics.ListAPIView):
    queryset = Office.objects.all()
    serializer_class = OfficeSerializer
    # permission_classes = (IsAuthenticated,)


class OfficeAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Office.objects.all()
    serializer_class = OfficeSerializer
    permission_classes = (IsAdminOrReadOnly,)


class OfficeAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Office.objects.all()
    serializer_class = OfficeSerializer
    permission_classes = (IsAuthenticated,)
    # authentication_classes = (TokenAuthentication,)