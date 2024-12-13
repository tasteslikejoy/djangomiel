from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializer import CandidateStatusSerializer, CandidateAllSerializer, OfficeAllSerializer
from .models import CandidateCard, Office, Status


# Получение количества кандидатов, которым принадлежит статус
class CandidateCountView(APIView):
    def get(self, request):
        statuses = Status.objects.all()
        serializer = CandidateStatusSerializer(statuses, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


# Сколько офисов требуют квоту
class OfficeCountView(APIView):
    def get(self, request):
        count = Office.objects.filter(quota__need__gt=0).count()
        return Response({'office_count_not_zero': count}, status=status.HTTP_200_OK)


# Всего кандидатов в базе
class CandidateAllView(APIView):
    def get(self, request):
        count = CandidateCard.objects.count()
        serializer = CandidateAllSerializer(data={'count': count})
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Всего офисов в базе
class OfficeAllView(APIView):
    def get(self, request):
        count = Office.objects.count()
        serializer = OfficeAllSerializer(data={'count': count})
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)






