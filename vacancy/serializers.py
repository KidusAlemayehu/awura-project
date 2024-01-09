from rest_framework import serializers
from .models import Vacancy,VacancyRequest

class VacancySerializer(serializers.ModelSerializer):
    class Meta:
        model=Vacancy
        fields='__all__'
        
class VacancyRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = VacancyRequest
        fields = '__all__'
