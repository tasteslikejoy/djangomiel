from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import GenericViewSet
from .serializer import CandidateStatusSerializer
from .models import CandidateCard


# Получение количества кандидатов, которым принадлежит статус
class CandidateCountView(APIView):
    def get(self, request, status_id):
        count = CandidateCard.objects.filter(invitation_to_office__status_id=status_id).count()
        serializer = CandidateStatusSerializer(data={'status_id': status_id, 'count': count})
        serializer.is_valid(raise_exception=True)

        return Response(serializer.data, status=status.HTTP_200_OK)






