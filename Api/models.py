from django.db import models

class ServerPod_1(models.Model):
    name = models.CharField(max_length=100)
    name1 = models.CharField(max_length=100)
  


class ServerPod_2(models.Model):
    name = models.CharField(max_length=100)
    name1 = models.CharField(max_length=100)
  
class ServerPod_3(models.Model):
    name = models.CharField(max_length=100)
    name1 = models.CharField(max_length=100)
  
class ServerPod_4(models.Model):
    name = models.CharField(max_length=100)
    name1 = models.CharField(max_length=100)

class ServerPod_5(models.Model):
    name = models.CharField(max_length=100)
    name1 = models.CharField(max_length=100)
  

class Megapod(models.Model):
    Megapod_description = models.CharField(max_length=100)
    ServerPod_1 = models.ForeignKey(ServerPod_1, related_name='matches', on_delete =models.CASCADE,blank=True, null=True)
    ServerPod_2 = models.ForeignKey(ServerPod_2, related_name='matches', on_delete =models.CASCADE,blank=True, null=True)
    ServerPod_3 = models.ForeignKey(ServerPod_3, related_name='matches', on_delete =models.CASCADE,blank=True, null=True)
    ServerPod_4 = models.ForeignKey(ServerPod_4, related_name='matches', on_delete =models.CASCADE,blank=True, null=True)
    ServerPod_5 = models.ForeignKey(ServerPod_5, related_name='matches', on_delete =models.CASCADE,blank=True, null=True)
    class Meta:
        verbose_name_plural = 'Megapod'
    def __str__(self):
        return self.Megapod_description
