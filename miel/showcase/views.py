from django.db.models import Model
from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import PersonalInfo, CandidateCard
from .serializers import PersonalInfoSerializer


# class CardCandidateAPIView(generics.ListAPIView):
#     queryset = PersonalInfo.objects.all()
#     serializer_class = PersonalInfoSerializer

class PersonalInfoAPIList(generics.ListCreateAPIView):
    queryset = PersonalInfo.objects.all()
    serializer_class = PersonalInfoSerializer


class PersonaInfoAPIView(APIView):
    def get(self, request):
        p = PersonalInfo.objects.all()   # .values()
        return Response({'posts': PersonalInfoSerializer(p, many=True).data})

    def post(self, request):
        serializer = PersonalInfoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        # return Response({'post': model_to_dict(post_new)})
        return Response({'post': serializer.data})

    def put(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({'error': 'Method PUT not allowed'})
        try:
            instance = PersonalInfo.objects.get(pk=pk)
        except:
            return Response({'error': 'Object does not exist'})

        serializer = PersonalInfoSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'post': serializer.data})

    def delete(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({'error': 'Method DELETE not allowed'})
        serializer = PersonalInfo.objects.get(pk=pk)
        serializer.delete(  )

        return Response({"post": 'delete post' + str(pk)})
