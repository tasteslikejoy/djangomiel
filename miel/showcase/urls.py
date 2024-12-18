"""
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from users.views import CreateAdminUserViewset
from showcase.views import (UserShowcaseRedirectView, CandidateCardViewset,
                            CandidateCountView, OfficeCountView, CandidateAllView, OfficeAllView, QuotaChangeView,
                            AdminShowcaseViewSet, SuperviserShowcaseViewSet, QuotaHistoryView,
                            ArchiveCandidatesView, InvitedCandidatesView, RejectedCandidateView,
                            StatusCreateUpdateDeleteViewSet, SkillCreateUpdateDeleteViewSet,
                            CourseCreateUpdateDeleteViewSet, InvitationsViewset, SetAdminLinkToAllOffices)

app_name = 'miel'

router = DefaultRouter()
router.register(r'cards', CandidateCardViewset, basename='cards')
router.register(r'admin_create', CreateAdminUserViewset, basename='admin_create')
router.register(r'invitations', InvitationsViewset, basename='invitations')

# Валераааа
router.register(r'showcase/administrator', AdminShowcaseViewSet, basename='showcase_administrator')
router.register(r'showcase/superviser', SuperviserShowcaseViewSet, basename='showcase_superviser')

# Алиса
router.register(r'statuses', StatusCreateUpdateDeleteViewSet, basename='statuses')  # создание, редактирование, удаление статусов
router.register(r'skills', SkillCreateUpdateDeleteViewSet, basename='skills')  # создание, редактирование, удаление навыков
router.register(r'course', CourseCreateUpdateDeleteViewSet, basename='course')  # создание, редактирование, удаление курсов

urlpatterns = [
    path('', include((router.urls, 'miel'), namespace='miel')),

    # Alex
    path('showcase/', UserShowcaseRedirectView.as_view(), name='showcase_user_redirect'),
    path('office/<int:pk>/quota_change/', QuotaChangeView.as_view(), name='quota_change'),
    path('send_admin_link/', SetAdminLinkToAllOffices.as_view(), name='send_admin_link'),

    # Alice
    path('candidate_status_count/', CandidateCountView.as_view(),
         name='candidate_status_count'),  # ссписок всех статусов и количества кандидатов по ним
    path('office_count/', OfficeCountView.as_view(), name='office_quota_count'),  # сколько офисов требуют квоту
    path('candidate_count/', CandidateAllView.as_view(), name='candidate_count'),  # сколько всего кандидатов INT
    path('office_all_count/', OfficeAllView.as_view(), name='office'),  # сколько всего офисов и инфо по ним
    path('offices/<int:office_id>/', OfficeAllView.as_view(), name='offices'),  # редактирование офиса
    path('quota_history/<int:office_id>/', QuotaHistoryView.as_view(), name='quota_history'),  # история квот
    path('candidate_archive/', ArchiveCandidatesView.as_view(), name='candidate_archive'),  # кандидаты в архиве
    path('candidate_invited/', InvitedCandidatesView.as_view(), name='candidate_invited'),  # новые приглашения
    path('candidate_rejected/', RejectedCandidateView.as_view(), name='candidate_rejected'),  # отклоненные
]
