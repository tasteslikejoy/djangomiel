from django.shortcuts import render
from rest_framework import viewsets, status, views
from .models import CandidateCard
from .serializers import CandidateCardSerializer, CandidateCardSerializerDirektor



class CandidateCardViewSet(viewsets.ModelViewSet):
    queryset = CandidateCard.objects.all()
    serializer_class = CandidateCardSerializer if user_role=='admin' else CandidateCardSerializerDirektor
    filterset_fields = ['id','created_at','current_workplace','current_occupation','employment_date',
                  'comment','favorite','archived','synopsis','objects_card','clients_card',
                  'invitation_to_office','experience','personal_info']

    def perform_create(self, serializer):
        serializer.save()

    def perform_update(self, serializer):
        serializer.save()



