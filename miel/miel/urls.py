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
from django.contrib import admin
from django.urls import path, include
from showcase.views import CandidateCountView, OfficeCountView, CandidateAllView, OfficeAllView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('djoser.urls.jwt')),
    path('auth/', include('djoser.urls')),
    path('api/v1/<int:status_id>', CandidateCountView.as_view(), name='candidate_status_count'), # сколько кандидатов на статус
    path('api/v1/office-count/', OfficeCountView.as_view(), name='office_quota_count'),  # сколько офисов требуют квоту
    path('api/v1/candidate-count/', CandidateAllView.as_view(), name='candidate_count'),  # сколько всего кандидатов
    path('api/v1/office_all-count/', OfficeAllView.as_view(), name='office'),  # сколько всего офисов
]
