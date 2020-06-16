from __future__ import unicode_literals
from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import generics


def thanks(request):  
    return render(request, 'thanks.html', )


#MegapodList View
class MegpapodListView(generics.ListCreateAPIView):
    queryset = Megapod.objects.all()
    serializer_class = MegapodDetailSerializer


class MegapodView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MegapodDetailSerializer
    queryset = Megapod.objects.all()

#megapod_detail_view
class Megpapod_Detail_ListView(generics.ListCreateAPIView):
    queryset = Megapod.objects.all()
    serializer_class = MegapodDetailSerializer


class Megpapod_Detail_View(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MegapodDetailSerializer
    queryset = Megapod.objects.all()

#ServerPod_1
class ServerPodListView_1(generics.ListCreateAPIView):
    queryset = ServerPod_1.objects.all()
    serializer_class = ServerPodSerializer_1


class ServerPodView_1(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ServerPodSerializer_1
    queryset = ServerPod_1.objects.all()

#ServerPod_2
class ServerPodListView_2(generics.ListCreateAPIView):
    queryset = ServerPod_2.objects.all()
    serializer_class = ServerPodSerializer_2


class ServerPodView_2(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ServerPodSerializer_2
    queryset = ServerPod_2.objects.all()

#ServerPod_3
class ServerPodListView_3(generics.ListCreateAPIView):
    queryset = ServerPod_3.objects.all()
    serializer_class = ServerPodSerializer_3


class ServerPodView_3(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ServerPodSerializer_3
    queryset = ServerPod_3.objects.all()


#ServerPod_4
class ServerPodListView_4(generics.ListCreateAPIView):
    queryset = ServerPod_4.objects.all()
    serializer_class = ServerPodSerializer_4


class ServerPodView_4(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ServerPodSerializer_4
    queryset = ServerPod_4.objects.all()


#ServerPod_5
class ServerPodListView_5(generics.ListCreateAPIView):
    queryset = ServerPod_5.objects.all()
    serializer_class = ServerPodSerializer_1


class ServerPodView_5(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ServerPodSerializer_5
    queryset = ServerPod_5.objects.all()

