from rest_framework import generics,permissions
from .models import Vacancy,VacancyRequest
from .serializers import VacancySerializer,VacancyRequestSerializer

from django.core.exceptions import PermissionDenied

class VacancyListCreateView(generics.ListCreateAPIView):
    queryset=Vacancy.objects.all()
    serializer_class=VacancySerializer
    permission_classes=[permissions.IsAuthenticatedOrReadOnly]
    
    def perform_create(self, serializer):
        if not self.request.user.is_staff:
            raise PermissionDenied("only admin can create vacancy posts")
        serializer.save()
class VacancyRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer
    def get_permissions(self):
        if self.request.method in ['GET']:
            return [permissions.AllowAny()]  # Allow anyone to retrieve (view) the vacancy
        else:
            return [permissions.IsAdminUser()]
    
class VacancyRequestCreateView(generics.CreateAPIView):
    queryset = VacancyRequest.objects.all()
    serializer_class = VacancyRequestSerializer
    permission_classes = [permissions.AllowAny]
class VacancyRequestListView(generics.ListAPIView):
    serializer_class = VacancyRequestSerializer
    permission_classes = [permissions.IsAdminUser]

    def get_queryset(self):
        vacancy_id = self.kwargs['pk']
        return VacancyRequest.objects.filter(vacancy_id=vacancy_id)
