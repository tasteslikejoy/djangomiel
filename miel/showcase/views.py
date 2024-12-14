from django.contrib.auth import get_user_model
from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.reverse import reverse_lazy, reverse
from rest_framework.views import APIView, status
from rest_framework.generics import ListCreateAPIView
from rest_framework import viewsets
from django.http import HttpResponseRedirect

from rest_framework.pagination import LimitOffsetPagination

from users.permissions import IsSuperAdministrator, IsAdministrator, IsSuperviser
from .models import CandidateCard, Office, Status
from .serializers import CandidateCardSerializer
from .serializer import CandidateStatusSerializer, CandidateAllSerializer, OfficeAllSerializer


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


class CardTestApiView(ListCreateAPIView):  # TODO убрать
    queryset = CandidateCard.objects.all()
    permission_classes = [IsSuperviser]
    serializer_class = CandidateCardSerializer
    pagination_class = LimitOffsetPagination


class CandidateCardViewset(viewsets.ModelViewSet):
    queryset = CandidateCard.objects.all()
    permission_classes = [IsSuperviser | IsAdministrator]
    pagination_class = LimitOffsetPagination
    serializer_class = CandidateCardSerializer

    def create(self, request, *args, **kwargs):
        if request.user.get_role() != User.UserRoles.administrator:
            return Response({
                'status': status.HTTP_405_METHOD_NOT_ALLOWED,
                'message': 'Method not allowed.'
            })
        else:
            return super().create(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        if request.user.get_role() != User.UserRoles.administrator:
            return Response({
                'status': status.HTTP_405_METHOD_NOT_ALLOWED,
                'message': 'Method not allowed.'
            })
        else:
            return super().partial_update(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return Response({
                'status': status.HTTP_405_METHOD_NOT_ALLOWED,
                'message': 'Method not allowed.'
            })

    def destroy(self, request, *args, **kwargs):
        if request.user.get_role() != User.UserRoles.administrator:
            return Response({
                'status': status.HTTP_405_METHOD_NOT_ALLOWED,
                'message': 'Method not allowed.'
            })
        else:
            return super().destroy(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):  # Нужна ли детализация?
        return super().retrieve(request, *args, **kwargs)

    @action(detail=True, methods=['patch'])
    def set_favorite(self, request, pk=None):
        card = self.get_object()
        card.favorite = True
        card.save()
        return Response({
            'status': status.HTTP_200_OK,
            'message': 'Карточка кандидата'
        })


class UserShowcaseRedirectView(APIView):
    permission_classes = [IsSuperviser | IsAdministrator]

    def get(self, request):
        user = request.user
        if user.get_role() == user.UserRoles.superviser:
            return Response({
                'status': status.HTTP_200_OK,
                'message': f'Вы вошли на страницу для роли {user.UserRoles.superviser.label}',
                'info': f'{user.get_role()}, {user.UserRoles.superviser}'
            })
        elif user.get_role() == user.UserRoles.administrator:
            return Response({
                'status': status.HTTP_200_OK,
                'message': f'Вы вошли на страницу для роли {user.UserRoles.administrator.label}',
                'info': f'{user.get_role()}, {user.UserRoles.administrator}'
            })
        elif user.get_role() == user.UserRoles.staff:
            # return HttpResponseRedirect(reverse('miel:test_api'))
            return HttpResponseRedirect(reverse_lazy('test_api'))


class TestApiView(APIView):
    def get(self, request):
        return Response({
            'You have been redirected'
        })


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
        return Response({'office_count_not_zero': count}, status=status.HTTP_200_OK)  # TODO


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
        offices = Office.objects.all()
        office_count = offices.count()
        serializer = OfficeAllSerializer(offices, many=True)
        data = {
            'count': office_count,
            'offices': serializer.data
        }
        return Response(data, status=status.HTTP_200_OK)  # TODO добавить в гет сколько офисов требуют квоту
