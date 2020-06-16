from rest_framework import serializers
from drf_writable_nested.serializers import WritableNestedModelSerializer


from Api.models import *
class ServerPodSerializer_5(serializers.ModelSerializer):
    class Meta:
        model = ServerPod_5
        fields = '__all__'

class ServerPodSerializer_4(serializers.ModelSerializer):
    class Meta:
        model = ServerPod_4
        fields = '__all__'


class ServerPodSerializer_3(serializers.ModelSerializer):
    class Meta:
        model = ServerPod_3
        fields = '__all__'

class ServerPodSerializer_2(serializers.ModelSerializer):
    class Meta:
        model = ServerPod_2
        fields = '__all__'


class ServerPodSerializer_1(serializers.ModelSerializer):
    class Meta:
        model = ServerPod_1
        fields = '__all__'


class MegapodDetailSerializer(WritableNestedModelSerializer):
    ServerPod_1 = ServerPodSerializer_1( )
    ServerPod_2 = ServerPodSerializer_2( )
    ServerPod_3 = ServerPodSerializer_3()
    ServerPod_4 = ServerPodSerializer_4( )
    ServerPod_5 = ServerPodSerializer_5( )
    
    class Meta:
        model = Megapod
        fields = ('id' ,'Megapod_description', 'ServerPod_1','ServerPod_2','ServerPod_3','ServerPod_4','ServerPod_5')

    def create(self, validated_data):
        print(validated_data)
        ServerPod_1 = validated_data.pop('ServerPod_1')
        ServerPod_2 = validated_data.pop('ServerPod_2')
        ServerPod_3 = validated_data.pop('ServerPod_3')
        ServerPod_4 = validated_data.pop('ServerPod_4')
        ServerPod_5 = validated_data.pop('ServerPod_5')

        Megapod = Megapod.objects.create(**validated_data)
        for ServerPod_1 in ServerPod_1:
            ServerPod_1.objects.create(Megapod=Megapod, **ServerPod_1)

        for ServerPod_2 in ServerPod_2:
            ServerPod_2.objects.create(Megapod=Megapod, **ServerPod_2)

        for ServerPod_3 in ServerPod_3:
            ServerPod_3.objects.create(Megapod=Megapod, **ServerPod_3)

        for ServerPod_4 in ServerPod_4:
            ServerPod_4.objects.create(Megapod=Megapod, **ServerPod_4)

        for ServerPod_5 in ServerPod_5:
            ServerPod_5.objects.create(Megapod=Megapod, **ServerPod_5)
        return Megapod


    
