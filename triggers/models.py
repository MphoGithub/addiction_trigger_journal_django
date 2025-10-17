from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Trigger(models.Model):
    CATEGORY_CHOICES = [
        ('Emotional','Emotional'),
        ('Environmental','Environmental'),
        ('Physical','Physical'),
        ('Psychological','Psychological'),
        ('Other','Other'),
    ]
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=False)
    category = models.CharField(max_length=50,choices=CATEGORY_CHOICES,blank=False)
    coping_strategy = models.TextField(blank=True)
    date_logged = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.name} - {self.category}"