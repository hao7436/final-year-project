from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework import mixins
from .models import *
from .serializers import *

class StoriesList(generics.ListAPIView):
    queryset = Stories.objects.all()
    serializer_class = StoriesSerializer



class CooperationList(generics.ListAPIView):
    queryset = Cooperation.objects.all()
    serializer_class = CooperationSerializer


class JoinActivitesList(generics.ListAPIView):
    queryset = JoinActivites.objects.all()
    serializer_class = JoinActivitesSerializer



class StoriesDetails(mixins.CreateModelMixin, 
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    queryset = Stories.objects.all()
    serializer_class = StoriesSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


        