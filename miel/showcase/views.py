import django_filters
from django.contrib.auth import get_user_model
from drf_spectacular.utils import extend_schema, extend_schema_serializer, extend_schema_view
from rest_framework.decorators import action
from rest_framework.exceptions import MethodNotAllowed
from rest_framework.response import Response
from rest_framework.views import APIView, status
from rest_framework import viewsets
from django.http import HttpResponseRedirect
from rest_framework import generics
from rest_framework.pagination import LimitOffsetPagination

from users.permissions import IsSuperAdministrator, IsAdministrator, IsSuperviser
from .models import CandidateCard, Office, Status, Quota, Invitations
from .serializers import (CandidateCardSerializer, CandidateStatusSerializer, CandidateAllSerializer,
                          OfficeAllSerializer, AdminShowcaseSerializer, SuperviserShowcaseSerializer, QuotaSerializer, InvitationSerializer)

User = get_user_model()


@extend_schema(tags=['API для работы с карточками кандидатов'])
class CandidateCardViewset(viewsets.ModelViewSet):
    queryset = CandidateCard.objects.all()
    permission_classes = [IsSuperviser | IsAdministrator]
    pagination_class = LimitOffsetPagination
    serializer_class = CandidateCardSerializer

    @extend_schema(summary='Создание карточки кандидата.')
    def create(self, request, *args, **kwargs):
        if request.user.get_role() != User.UserRoles.administrator:
            return Response({
                'status': status.HTTP_405_METHOD_NOT_ALLOWED,
                'message': 'Method not allowed.'
            })
        else:
            return super().create(request, *args, **kwargs)

    @extend_schema(summary='Частичное изменение карточки кандидата.')
    def partial_update(self, request, *args, **kwargs):
        if request.user.get_role() != User.UserRoles.administrator:
            return Response({
                'status': status.HTTP_405_METHOD_NOT_ALLOWED,
                'message': 'Method not allowed.'
            })
        else:
            return super().partial_update(request, *args, **kwargs)

    @extend_schema(exclude=True)
    def update(self, request, *args, **kwargs):
        return Response({
            'status': status.HTTP_405_METHOD_NOT_ALLOWED,
            'message': 'Method not allowed.'
        })

    @extend_schema(summary='Удаление карточки кандидата.')
    def destroy(self, request, *args, **kwargs):
        if request.user.get_role() != User.UserRoles.administrator:
            return Response({
                'status': status.HTTP_405_METHOD_NOT_ALLOWED,
                'message': 'Method not allowed.'
            })
        else:
            return super().destroy(request, *args, **kwargs)

    @extend_schema(summary='Список карточек кандидата.')
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @extend_schema(summary='Детальная информация по карточке кандидата.')
    def retrieve(self, request, *args, **kwargs):  # Нужна ли детализация?
        return super().retrieve(request, *args, **kwargs)

    @extend_schema(exclude=True)
    @action(detail=True, methods=['patch'])
    def set_favorite(self, request, pk=None):  # FIXME переделать логику см. правки
        card = self.get_object()
        card.favorite = True
        card.save()
        return Response({
            'status': status.HTTP_200_OK,
            'message': 'Карточка кандидата'
        })


@extend_schema(tags=['API витрина кандидатов'])
class UserShowcaseRedirectView(APIView):  # TODO доделать ссылки на редирект
    """Основное URL для автоматического перехода на нужное представление Витрины Кандидатов """
    permission_classes = [IsSuperviser | IsAdministrator]

    @extend_schema(summary='Основное представление с автоматическим переходом на  URL представления '
                           'Витринцы кандидатов, в зависимости от роли пользователя который делал запрос.')
    def get(self, request):
        user = request.user
        if user.get_role() == user.UserRoles.superviser:
            return HttpResponseRedirect(redirect_to='/api/v1/showcase/superviser/')
        elif user.get_role() == user.UserRoles.administrator:
            return HttpResponseRedirect(redirect_to='/api/v1/showcase/administrator/')
        elif user.get_role() == user.UserRoles.staff:
            return Response({
                'status': status.HTTP_200_OK,
                'message': f'Вы вошли на страницу для роли {user.UserRoles.staff.label}'
            })


@extend_schema(tags=['API вспомогательные'])
class CandidateCountView(APIView):
    @extend_schema(summary='Получение всех статусов и количества карточек которые к ним привязаны.')
    def get(self, request):
        statuses = Status.objects.all()
        serializer = CandidateStatusSerializer(statuses, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


@extend_schema(tags=['API вспомогательные'])
class OfficeCountView(APIView):
    @extend_schema(summary='Отображение количества офисов у которых есть потребность в квоте.')
    def get(self, request):
        count = Office.objects.filter(quotas__need__gt=0).count()
        return Response({'office_count_not_zero': count}, status=status.HTTP_200_OK)  # TODO


@extend_schema(tags=['API вспомогательные'])
class CandidateAllView(APIView):
    @extend_schema(summary='Отображение количество карточек кандидатов в базе.')
    def get(self, request):
        count = CandidateCard.objects.count()
        serializer = CandidateAllSerializer(data={'count': count})
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@extend_schema(tags=['API вспомогательные'])
class OfficeAllView(APIView):
    @extend_schema(summary='Отображение количества и данных офисов.')
    def get(self, request):
        offices = Office.objects.all()
        office_count = offices.count()
        serializer = OfficeAllSerializer(offices, many=True)
        data = {
            'count': office_count,
            'offices': serializer.data
        }
        return Response(data, status=status.HTTP_200_OK)  # TODO добавить в гет сколько офисов требуют квоту

    @extend_schema(summary='Редактирование данных офиса.')
    def put(self, request, office_id):
        try:
            office = Office.objects.get(id=office_id)
        except Office.DoesNotExist:
            return Response({'error': 'Офис не найден'}, status=status.HTTP_404_NOT_FOUND)

        serializer = OfficeAllSerializer(office, data=request.data)
        if serializer.is_valid():
            update_office = serializer.save()
            return Response(OfficeAllSerializer(update_office).data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class QuotaHistoryView(APIView):
    def get(self, request, office_id):
        quotas = Quota.objects.filter(office_id=office_id)
        invitations_invited = Invitations.objects.filter(status__name='Приглашен')
        invitations_hired = Invitations.objects.filter(status__name='Принят в штат')

        quota_data = QuotaSerializer(quotas, many=True).data

        quota_creation_dates = [quota['date'] for quota in quota_data]
        quota_quantities = [quota['quantity'] for quota in quota_data]
        quota_used = [quota['used'] for quota in quota_data]

        invitation_data_invited = InvitationSerializer(invitations_invited, many=True).data
        invitation_data_hired = InvitationSerializer(invitations_hired, many=True).data

        response_data = {
            'quota_creation_dates': quota_creation_dates,
            'quota_quantities': quota_quantities,
            'quota_used': quota_used,
            'invitations_invited': invitation_data_invited,
            'invitations_hired': invitation_data_hired
        }

        return Response(response_data, status=status.HTTP_200_OK)


# Валераааа

@extend_schema(tags=['API витрина кандидатов'])
@extend_schema_view(retrieve=extend_schema(exclude=True),
                    list=extend_schema(summary='Отображение витрины кандидатов для администратора.'))
class AdminShowcaseViewSet(viewsets.ModelViewSet):
    queryset = CandidateCard.objects.all().order_by('id')
    serializer_class = AdminShowcaseSerializer
    filterset_fields = ['id', 'created_at', 'current_workplace', 'current_occupation', 'employment_date',
                        'comment', 'favorite', 'archived', 'synopsis', 'objects_card', 'clients_card',
                        'invitation_to_office', 'experience', 'personal_info']
    http_method_names = ['get']

    # def get_queryset(self):
    #     user = self.request.user
    #     if user.get_role is user.UserRoles.administrator:
    #         queryset = CandidateCard.objects.filter(
    #             id__in=[2, 3]).order_by('created_at', 'favorite')  # FIXME переделать фильтр id на фильтр id статусов
    #     else:
    #         queryset = None
    #     # queryset = CandidateCard.objects.filter(id__in=[2, 3]).order_by('created_at', 'favorite')
    #     return queryset


@extend_schema(tags=['API витрина кандидатов'])
@extend_schema_view(retrieve=extend_schema(exclude=True),
                    list=extend_schema(summary='Отображение витрины кандидатов для руководителя.'))
class SuperviserShowcaseViewSet(viewsets.ModelViewSet):
    queryset = CandidateCard.objects.all().order_by('id')
    serializer_class = SuperviserShowcaseSerializer
    # filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['id', 'created_at', 'current_workplace', 'personal_info']
    http_method_names = ['get']

    # def get_queryset(self):
    #     user = self.request.user
    #     if user.get_role is user.UserRoles.administrator:
    #         queryset = CandidateCard.objects.filter(
    #             id__in=[2, 3]).order_by('created_at', 'favorite')  # FIXME переделать фильтр id на фильтр id статусов
    #     elif user.get_role is user.UserRoles.superviser:
    #         queryset = CandidateCard.objects.filter(
    #             id__in=[2, 3]).order_by('created_at', 'favorite')  # FIXME переделать фильтр id на фильтр id статусов
    #     else:
    #         queryset = None
    #     # queryset = CandidateCard.objects.filter(id__in=[2,3]).order_by('created_at','favorite')
    #     return queryset


