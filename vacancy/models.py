from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Vacancy(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField()
    release_date=models.DateField()
    end_date=models.DateField()
    form_Link=models.URLField()
    is_open=models.BooleanField(default=True)
    
    
    
    def __str__(self):
        return self.title

class VacancyRequest(models.Model):
    vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True) 
