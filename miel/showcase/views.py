from django.shortcuts import render
import django_filters
from rest_framework import viewsets, status, views
from .models import CandidateCard, PersonalInfo
from .serializers import CandidateCardSerializer, CandidateCardSerializerDirektor



class CandidateCardViewSet(viewsets.ModelViewSet):
    queryset = CandidateCard.objects.all().order_by('id')
    serializer_class = CandidateCardSerializer
    filterset_fields = ['id','created_at','current_workplace','current_occupation','employment_date',
                  'comment','favorite','archived','synopsis','objects_card','clients_card',
                  'invitation_to_office','experience','personal_info']

    def get_queryset(self):
        if self.request.user.id is admin:
            queryset = CandidateCard.objects.filter(id__in=[2, 3]).order_by('created_at', 'favorite')
        else:
            queryset = None
        #queryset = CandidateCard.objects.filter(id__in=[2, 3]).order_by('created_at', 'favorite')
        return queryset

from rest_framework import filters
class CandidateCardViewSetDirektor(viewsets.ModelViewSet):
    serializer_class = CandidateCardSerializerDirektor
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['id','created_at','current_workplace','personal_info']

    def get_queryset(self):
        if self.request.user.id is admin:
            queryset = CandidateCard.objects.filter(id__in=[2, 3]).order_by('created_at', 'favorite')
        elif self.request.user.id is direktor:
            queryset = CandidateCard.objects.filter(id__in=[2, 3]).order_by('created_at', 'favorite')
        else:
            queryset = None
        #queryset = CandidateCard.objects.filter(id__in=[2,3]).order_by('created_at','favorite')
        return queryset



