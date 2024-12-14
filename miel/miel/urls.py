"""
URL configuration for miel project.

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
# from django.conf import settings
# from django.conf.urls.static import static
# import djoser  # надо ли?

from django.contrib import admin
from django.urls import path, include, re_path

# from users.views import CreateAdminUserView
from users.views import CreateAdminUserViewset
from showcase.views import CardTestApiView, UserShowcaseRedirectView, CandidateCardViewset, TestApiView
from showcase.views import CandidateCountView, OfficeCountView, CandidateAllView, OfficeAllView
from showcase.views import *  # ПОПРАВИТЬ!!!!ЙЙЙЙЙЙ


from rest_framework.routers import DefaultRouter

app_name = 'miel'

router = DefaultRouter()
router.register(r'cards', CandidateCardViewset, basename='cards')
router.register(r'admin_create', CreateAdminUserViewset, basename='admin_create')

# router = MyCustomRouter()
# router.register(r'personal_info', PersonalInfoViewSet, basename='personal_info')
# print(router.urls)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('auth/', include('djoser.urls.jwt')),
    path('auth/', include('djoser.urls')),
    # path('admin_create/', CreateAdminUserView.as_view(), name='admin_create'),
    path('test/', TestApiView.as_view(), name='test_api'),  # Тест редиректа
    path('test_cards/', CardTestApiView.as_view(), name='card_test_api'),
    path('showcase/', UserShowcaseRedirectView.as_view(), name='showcase_user_redirect')
    # Alice
    path('api/v1/', CandidateCountView.as_view(), name='candidate_status_count'), # сколько кандидатов на статус
    path('api/v1/office-count/', OfficeCountView.as_view(), name='office_quota_count'),  # сколько офисов требуют квоту
    path('api/v1/candidate-count/', CandidateAllView.as_view(), name='candidate_count'),  # сколько всего кандидатов
    path('api/v1/office_all-count/', OfficeAllView.as_view(), name='office'),  # сколько всего офисов
    # Igor
    # path('api/v1/', include(router.urls)),
    path('api/v1/drf-auth/', include('rest_framework.urls')),

    path('api/v1/personal_info/', PersonalInfoAPIList.as_view()),
    path('api/v1/offices/', OfficeListAPI.as_view()),

    path('api/v1/personal_info/<int:pk>/', PersonalInfoAPIUpdate.as_view()),
    path('api/v1/offices/<int:pk>/', OfficeAPIUpdate.as_view()),

    path('api/v1/personal_info_delete/<int:pk>/', PersonalInfoAPIDestroy.as_view()),
    path('api/v1/office_delete/<int:pk>/', OfficeAPIDestroy.as_view()),

    path('api/v1/auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
    path('api/v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v1/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    # path('api/v1/personal_info_card/', PersonalInfoViewSet.as_view({'get': 'list'})),
    # path('api/v1/personal_info_card/<int:pk>/', PersonalInfoViewSet.as_view({'get': 'update'})),

]
# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
