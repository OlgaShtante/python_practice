from django.db import models
from vehicles.models import Tanks
class Players(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    date_joined = models.DateTimeField(auto_now_add=True)

class PlayerVehicles(models.Model):
    id = models.AutoField(primary_key=True)
    player_id = models.ForeignKey(Players, on_delete=models.CASCADE)
    vehicle_id = models.ForeignKey(Tanks, on_delete=models.CASCADE)
    experience_points = models.IntegerField()