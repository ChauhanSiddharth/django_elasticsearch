from django.db import models

# Create your models here.
class Car(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    type = models.IntegerField(choices=[
        (1, "Sedan"),
        (2, "Truck"),
        (4, "SUV"),
    ])

    def __str__(self):
        return self.name

        
    
        
    