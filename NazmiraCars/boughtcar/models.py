from django.db import models
from carbrands.models import Car, Brand
from user.forms import User
# Create your models here.
class BoughtCar(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.owner.username} {self.car.name}"