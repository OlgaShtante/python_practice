from django.db import models

class Tanks(models.Model):
    LIGHT = 'light'
    MEDIUM = 'medium'
    HEAVY = 'heavy'
    TANK_TYPE_CHOICES = [
        (LIGHT, 'Легкий'),
        (MEDIUM, 'Средний'),
        (HEAVY, 'Тяжелый'),
    ]
    id = models.AutoField(primary_key=True)
    tank_name = models.CharField(max_length=100)
    tank_type = models.CharField(max_length=10, choices=TANK_TYPE_CHOICES)
    tank_description = models.TextField()
    damage_points = models.IntegerField()
    armor_points = models.IntegerField()
    speed = models.DecimalField(max_digits=5, decimal_places=2)
    cost = models.DecimalField(max_digits=10, decimal_places=2)