from django.shortcuts import render

from trvaelblogs import models
from .serializers import TravelBlogsSerializer,TravelPlaceSerializer,FoodSerializer,DramaSerializer,AboutSerializer

from rest_framework import generics

# Create your views here.


class ListTravelBlog(generics.ListCreateAPIView):
    queryset = models.TravelBlog.objects.all()
    serializer_class = TravelBlogsSerializer


class DetailTravelBlog(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.TravelBlog.objects.all()
    serializer_class = TravelBlogsSerializer



class ListTravelPlace(generics.ListCreateAPIView):
    queryset = models.TravelPlace.objects.all()
    serializer_class = TravelPlaceSerializer


class DetailTravelPlace(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.TravelPlace.objects.all()
    serializer_class = TravelPlaceSerializer




class ListFood(generics.ListCreateAPIView):
    queryset = models.Food.objects.all()
    serializer_class = FoodSerializer


class DetailFood(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Food.objects.all()
    serializer_class = FoodSerializer






class ListDrama(generics.ListCreateAPIView):
    queryset = models.Drama.objects.all()
    serializer_class = DramaSerializer


class DetailDrama(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Drama.objects.all()
    serializer_class = DramaSerializer





class ListAbout(generics.ListCreateAPIView):
    queryset = models.About.objects.all()
    serializer_class = AboutSerializer


class DetailAbout(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.About.objects.all()
    serializer_class = AboutSerializer