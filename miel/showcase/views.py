from django.contrib.auth import get_user_model
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView, status
from rest_framework.generics import ListCreateAPIView
from rest_framework import viewsets

from users.permissions import IsSuperAdministrator, IsAdministrator, IsSuperviser
from .models import CandidateCard
from .serializers import CandidateCardSerializer

User = get_user_model()


# Create your views here.


# class CardTestApiView(APIView):
#     permission_classes = [IsSuperviser]
#
#     def get(self, request):
#         cards = CandidateCard.objects.all()
#         serializer = CandidateCardSerializer(cards, many=True)
#
#         return Response({
#             'status': status.HTTP_200_OK,
#             'data': serializer.data,
#         })


class CardTestApiView(ListCreateAPIView):
    queryset = CandidateCard.objects.all().prefetch_related()
    # permission_classes = [IsSuperviser]
    serializer_class = CandidateCardSerializer
    #
    # def get(self, request, *args, **kwargs):
    #     cards = CandidateCard.objects.all()
    #     serializer = CandidateCardSerializer(cards, many=True)
    #
    #     return Response({
    #         'status': status.HTTP_200_OK,
    #         'data': serializer.data,
    #     })
