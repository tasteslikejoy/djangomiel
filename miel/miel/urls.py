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

from showcase.views import *
from rest_framework import routers


# @action(methods=["get"], detail=False)
# def office(self, request):
#     off = Office.objects.all()
#     return Response({'off': [c.name for c in off]})

# class MyCustomRouter(routers.SimpleRouter):
#     routes = [
#         routers.Route(url=r'^{prefix}$',
#                       mapping={'get': 'list'},
#                       name='{basename}-list',
#                       detail=False,
#                       initkwargs={'suffix': 'List'}),
#         routers.Route(url=r'^{prefix}/{lookup}$',
#                       mapping={'get': 'retrieve'},
#                       name='{basename}-detail',
#                       detail=True,
#                       initkwargs={'suffix': 'Detail'})
#     ]


# router = MyCustomRouter()
# router.register(r'personal_info', PersonalInfoViewSet, basename='personal_info')
# print(router.urls)




urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api/v1/', include(router.urls)),
    path('api/v1/personal_info/', PersonalInfoAPIList.as_view()),
    path('api/v1/personal_info/<int:pk>/', PersonalInfoAPIUpdate.as_view()),
    path('api/v1/personal_info_delete/<int:pk>/', PersonalInfoAPIDestroy.as_view())
    # path('api/v1/personal_info_card/', PersonalInfoViewSet.as_view({'get': 'list'})),
    # path('api/v1/personal_info_card/<int:pk>/', PersonalInfoViewSet.as_view({'get': 'update'})),

]
