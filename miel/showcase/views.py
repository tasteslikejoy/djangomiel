from django.contrib.auth import get_user_model
from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView, status
from rest_framework.generics import GenericAPIView
from rest_framework import viewsets
from django.http import HttpResponseRedirect
from rest_framework import generics
from rest_framework.pagination import LimitOffsetPagination

from users.permissions import IsAdministrator, IsSuperviser
from .models import CandidateCard, Office, Status, Quota, Favorites, Invitations, Skill, Course
from .serializers import (CandidateCardSerializer, CandidateStatusSerializer, CandidateAllSerializer,
                          OfficeAllSerializer, AdminShowcaseSerializer, SuperviserShowcaseSerializer,
                          QuotaAutoCreateSerializer, QuotaSerializer, InvitationSerializer, StatusSerializer, SkillSerializer,
                          CoursesSerializer)

User = get_user_model()


@extend_schema(tags=['API для работы с карточками кандидатов'])
class CandidateCardViewset(viewsets.ModelViewSet):
    queryset = CandidateCard.objects.all()
    permission_classes = [IsSuperviser | IsAdministrator]
    pagination_class = LimitOffsetPagination
    serializer_class = CandidateCardSerializer

    @extend_schema(summary='Создание карточки кандидата. A')
    def create(self, request, *args, **kwargs):
        if request.user.get_role() != User.UserRoles.administrator:
            return Response({
                'status': status.HTTP_405_METHOD_NOT_ALLOWED,
                'message': 'Method not allowed.'
            })
        else:
            return super().create(request, *args, **kwargs)

    @extend_schema(summary='Частичное изменение карточки кандидата. A')
    def partial_update(self, request, *args, **kwargs):
        if request.user.get_role() != User.UserRoles.administrator:
            return Response({
                'status': status.HTTP_405_METHOD_NOT_ALLOWED,
                'message': 'Method not allowed.'
            })
        else:
            return super().partial_update(request, *args, **kwargs)

    @extend_schema(summary='Полное изменение карточки кандидата. A')
    def update(self, request, *args, **kwargs):
        if request.user.get_role() != User.UserRoles.administrator:
            return Response({
                'status': status.HTTP_405_METHOD_NOT_ALLOWED,
                'message': 'Method not allowed.'
            })
        else:
            return super().update(request, *args, **kwargs)

    @extend_schema(summary='Удаление карточки кандидата. A')
    def destroy(self, request, *args, **kwargs):
        if request.user.get_role() != User.UserRoles.administrator:
            return Response({
                'status': status.HTTP_405_METHOD_NOT_ALLOWED,
                'message': 'Method not allowed.'
            })
        else:
            return super().destroy(request, *args, **kwargs)

    @extend_schema(summary='Список карточек кандидатов. A|S')
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @extend_schema(summary='Детальная информация по карточке кандидата. A|S')
    def retrieve(self, request, *args, **kwargs):  # Нужна ли детализация?
        return super().retrieve(request, *args, **kwargs)

    @extend_schema(summary='Добавление карточки в избранное. S')
    @action(detail=True, methods=['get'])
    def add_favorite(self, request, pk=None):
        if request.user.get_role() != User.UserRoles.superviser:
            return Response({
                'status': status.HTTP_405_METHOD_NOT_ALLOWED,
                'message': 'Метод только для действующих руководителей офисов.'
            })

        card = self.get_object()
        try:
            office = Office.objects.get(superviser=request.user)
        except Office.DoesNotExist:
            return Response({
                'status': status.HTTP_404_NOT_FOUND,
                'message': 'У данного пользователя нет офиса для работы с избранным.'
            })
        favorite = Favorites.objects.create(
            candidate_card=card,
            office=office
        )
        favorite.save()
        return Response({
            'status': status.HTTP_200_OK,
            'message': 'Карточка кандидата добавлена в избранное.'
        })

    @extend_schema(summary='Удаление карточки из избранного. S')
    @action(detail=True, methods=['get'])
    def remove_favorite(self, request, pk=None):
        if request.user.get_role() != User.UserRoles.superviser:
            return Response({
                'status': status.HTTP_405_METHOD_NOT_ALLOWED,
                'message': 'Метод только для действующих руководителей офисов.'
            })

        card = self.get_object()
        try:
            office = Office.objects.get(superviser=request.user)
        except Office.DoesNotExist:
            return Response({
                'status': status.HTTP_404_NOT_FOUND,
                'message': 'У данного пользователя нет офиса для работы с избранным.'
            })
        favorite = Favorites.objects.filter(office=office, candidate_card=card)
        if favorite.exists():
            favorite.delete()
        return Response({
            'status': status.HTTP_200_OK,
            'message': 'Карточка кандидата удалена из избранного.'
        })

    @extend_schema(summary='Список избранных карточек кандидата. S')
    @action(detail=False, methods=['get'])
    def favorite_list(self, request, *args, **kwargs):
        if request.user.get_role() != User.UserRoles.superviser:
            return Response({
                'status': status.HTTP_405_METHOD_NOT_ALLOWED,
                'message': 'Метод только для действующих руководителей офисов.'
            })

        try:
            office = Office.objects.get(superviser=request.user)
        except Office.DoesNotExist:
            return Response({
                'status': status.HTTP_404_NOT_FOUND,
                'message': 'У данного пользователя нет офиса для работы с избранным.'
            })

        queryset = CandidateCard.objects.filter(favorites__office=office).prefetch_related('favorites')

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @extend_schema(summary='Создание приглашения кандидата в офис. S')
    @action(detail=True, methods=['post'])
    def create_invitation(self, request, pk=None, *args, **kwargs):
        if request.user.get_role() != User.UserRoles.superviser:
            return Response({
                'status': status.HTTP_405_METHOD_NOT_ALLOWED,
                'message': 'Метод только для действующих руководителей офисов.'
            })
        office = Office.objects.filter(superviser=request.user)
        if office.exists():
            office = office.first()

            try:
                card = CandidateCard.objects.get(pk=pk)
            except ModuleNotFoundError:
                return Response({
                    'status': status.HTTP_400_BAD_REQUEST,
                    'message': 'Карточка кандидата не существует или ошибка в коде.'
                })

            invitation = Invitations.objects.filter(office=office, candidate_card=card)
            if invitation.exists():
                return Response({
                    'status': status.HTTP_304_NOT_MODIFIED,
                    'message': 'Приглашение в офис для этого кандидата уже создано.'
                })

            invitation = Invitations.objects.create(
                office=office,
                status=Status.objects.get(name='Приглашен'),
                candidate_card=card
            )
            return Response({
                'status': status.HTTP_201_CREATED,
                'message': f'Приглашение создано {invitation.id}'
            })
        else:
            return Response({
                'message': f'У авторизированного пользователя нет офиса для приглашения.'
            })


@extend_schema(tags=['API витрина кандидатов'])
class UserShowcaseRedirectView(APIView):
    """Основное URL для автоматического перехода на нужное представление Витрины Кандидатов """
    permission_classes = [IsSuperviser | IsAdministrator]

    @extend_schema(summary='Основное представление с автоматическим переходом на  URL представления '
                           'Витринцы кандидатов, в зависимости от роли пользователя который делал запрос. A|S')
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
    permission_classes = [IsSuperviser | IsAdministrator]

    @extend_schema(summary='Получение всех статусов и количества карточек которые к ним привязаны. A|S')
    def get(self, request):
        statuses = Status.objects.all()
        serializer = CandidateStatusSerializer(statuses, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


@extend_schema(tags=['API для работы с офисами'])
class OfficeCountView(APIView):
    permission_classes = [IsAdministrator]

    @extend_schema(summary='Отображение количества офисов у которых есть потребность в квоте. A')
    def get(self, request):
        count = Office.objects.filter(quotas__need__gt=0).count()
        return Response({'office_count_not_zero': count}, status=status.HTTP_200_OK)  # TODO


@extend_schema(tags=['API вспомогательные'])
class CandidateAllView(APIView):
    permission_classes = [IsSuperviser | IsAdministrator]

    @extend_schema(summary='Отображение количество карточек кандидатов в базе. A|S')
    def get(self, request):
        count = CandidateCard.objects.count()
        serializer = CandidateAllSerializer(data={'count': count})
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@extend_schema(tags=['API для работы с офисами'])
class OfficeAllView(APIView):
    permission_classes = [IsAdministrator]

    @extend_schema(summary='Отображение количества и данных офисов. A')
    def get(self, request, *args, **kwargs):
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

    @extend_schema(summary='Создание нового офиса.')
    def post(self, request, *args, **kwargs):
        serializer = OfficeAllSerializer(data=request.data)
        if serializer.is_valid():
            new_office = serializer.save()
            return Response(OfficeAllSerializer(new_office).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@extend_schema(tags=['API вспомогательные'])
class QuotaHistoryView(APIView):
    permission_classes = [IsAdministrator | IsSuperviser]

    @extend_schema(summary='История квот. A|S')
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


@extend_schema(tags=['API вспомогательные'])
@extend_schema_view(retrieve=extend_schema(exclude=True),
                    get=extend_schema(summary='Получение кандидатов из архива. A'))
class ArchiveCandidatesView(generics.ListAPIView):
    permission_classes = [IsAdministrator]
    serializer_class = CandidateCardSerializer
    http_method_names = ['get']

    def get_queryset(self):
        return CandidateCard.objects.filter(
            cards__status__name='Принят в штат'
        ).exclude(
            cards__status__name='Приглашен'
        ).exclude(
            current_workplace__isnull=True
        )


@extend_schema(tags=['API вспомогательные'])
@extend_schema_view(retrieve=extend_schema(exclude=True),
                    get=extend_schema(summary='Получение новых приглашений. A'))
class InvitedCandidatesView(generics.ListAPIView):
    permission_classes = [IsAdministrator]
    serializer_class = InvitationSerializer
    http_method_names = ['get']

    def get_queryset(self):
        return Invitations.objects.filter(
            status__name='Приглашен'
        )


@extend_schema(tags=['API вспомогательные'])
@extend_schema_view(retrieve=extend_schema(exclude=True),
                    get=extend_schema(summary='Получение карточек кандидатов со статусом отклонено. A'))
class RejectedCandidateView(generics.ListAPIView):
    permission_classes = [IsAdministrator]
    serializer_class = CandidateCardSerializer
    http_method_names = ['get']

    def get_queryset(self):
        return CandidateCard.objects.filter(
            cards__status__name__in=['Не принят', 'Отклонено кандидатом']
        )


@extend_schema(tags=['API создание, редактирование, удаление статусов'])
class StatusCreateUpdateDeleteViewSet(viewsets.ModelViewSet):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
    permission_classes = [IsAdministrator]


@extend_schema(tags=['API создание, редактирование, удаление навыков'])
class SkillCreateUpdateDeleteViewSet(viewsets.ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    permission_classes = [IsAdministrator]


@extend_schema(tags=['API создание, редактирование, удаление курсов'])
class CourseCreateUpdateDeleteViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CoursesSerializer
    permission_classes = [IsAdministrator]


@extend_schema(tags=['API витрина кандидатов'])
@extend_schema_view(retrieve=extend_schema(exclude=True),
                    list=extend_schema(summary='Отображение витрины кандидатов для администратора. A'))
class AdminShowcaseViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdministrator]
    queryset = CandidateCard.objects.all().order_by('id')
    serializer_class = AdminShowcaseSerializer
    pagination_class = LimitOffsetPagination
    filterset_fields = ['id', 'created_at', 'current_workplace', 'current_occupation', 'employment_date',
                        'comment', 'archived', 'synopsis', 'objects_card', 'clients_card',
                        'experience', 'personal_info']
    http_method_names = ['get']


@extend_schema(tags=['API витрина кандидатов'])
@extend_schema_view(retrieve=extend_schema(exclude=True),
                    list=extend_schema(summary='Отображение витрины кандидатов для руководителя. S'))
class SuperviserShowcaseViewSet(viewsets.ModelViewSet):
    permission_classes = [IsSuperviser]
    queryset = CandidateCard.objects.all().order_by('id')
    serializer_class = SuperviserShowcaseSerializer
    pagination_class = LimitOffsetPagination
    filterset_fields = ['id', 'created_at', 'current_workplace', 'personal_info']
    http_method_names = ['get']


@extend_schema(tags=['API для работы с офисами'])
class QuotaChangeView(APIView):
    permission_classes = [IsAdministrator]

    @extend_schema(summary='Изменение квоты для конкретного офиса. A')
    def post(self, request, *args, **kwargs):
        serializer = QuotaAutoCreateSerializer(data=request.data)

        office = Office.objects.filter(pk=kwargs['pk'])
        if office.exists():
            office = office.first()

        office_quotas = office.quotas.order_by('-date')
        if office_quotas.exists():
            office_quotas = office_quotas.last()

        if serializer.is_valid():
            print(serializer.validated_data)
            quota = Quota.objects.create(
                **serializer.validated_data,
                used=office_quotas.used,
                need=office_quotas.need,
                office=office
            )
            return Response({
                'status': status.HTTP_201_CREATED,
                'message': f'Идентификатор новой квоты - {quota.id} для офиса {office.name}'
            })


@extend_schema(tags=['API для работы с карточками кандидатов'])
@extend_schema_view(partial_update=extend_schema(exclude=True))
class InvitationsViewset(viewsets.ModelViewSet):
    queryset = Invitations.objects.all()
    serializer_class = InvitationSerializer
    permission_classes = [IsAdministrator]
    http_method_names = ['patch']

    @extend_schema(summary='Редактирование приглашения кандидата в офис. A')
    @action(detail=True, methods=['patch'])
    def patch(self, request, pk=None, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            try:
                status_obj = serializer.validated_data['status']
                status_name = Status.objects.get(name=status_obj['name'])
            except ModuleNotFoundError:
                return Response({
                    'status': status.HTTP_400_BAD_REQUEST,
                    'message': 'Такого статуса нет в базе данных'
                })

            invitation = self.get_object()
            invitation.status = status_name
            invitation.save()
            return Response({
                'status': status.HTTP_200_OK,
                'message': f'Статус приглашения успешно изменен на "{status_name}".'
            })


@extend_schema(tags=['API вспомогательные'])
class SetAdminLinkToAllOffices(GenericAPIView):
    queryset = Office.objects.all()
    model = Office
    serializer_class = Office
    permission_classes = [IsAdministrator]

    @extend_schema(summary='Изменение ссылки на контакт с админом для всех офисов. A')
    def post(self, request):
        link = request.user.contact_link

        for office in self.get_queryset():
            office.link_to_admin = link
            office.save()

        return Response({
            'status': status.HTTP_200_OK,
            'message': 'Ссылка на админа успешно изменена.'
        })


