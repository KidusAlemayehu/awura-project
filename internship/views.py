from rest_framework import generics,permissions
from .models import Vacancy,VacancyRequest
from .serializers import VacancySerializer,VacancyRequestSerializer
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from django.core.exceptions import PermissionDenied
from rest_framework.authentication import TokenAuthentication


class AdminLoginView(APIView):
    def post(self,request,*args, **kwargs):
        username=request.data.get('username')
        password=request.data.get('password')
        
        user=authenticate(request,username=username,password=password)
        
        if user is not None and user.is_staff:
            token,created=Token.objects.get_or_create(user=user)
            return Response({'token':token.key},status=status.HTTP_200_OK)
        else:
            return Response({'error':"Invalid credentials or not an admin"})

class VacancyListCreateView(generics.ListCreateAPIView):
    queryset=Vacancy.objects.all()
    serializer_class=VacancySerializer
    permission_classes=[permissions.IsAuthenticatedOrReadOnly]
    authentication_classes=[TokenAuthentication]
    
    
    def perform_create(self, serializer):
        if not self.request.user.is_staff:
            raise PermissionDenied("only admin can create vacancy posts")
        serializer.save()
class VacancyRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer
    def get_permissions(self):
        if self.request.method in ['GET']:
            return [permissions.AllowAny()] 
        else:
            return [permissions.IsAdminUser()]
    
class VacancyRequestCreateView(generics.CreateAPIView):
    queryset = VacancyRequest.objects.all()
    serializer_class = VacancyRequestSerializer
    permission_classes = [permissions.AllowAny]
class VacancyRequestListView(generics.ListAPIView):
    serializer_class = VacancyRequestSerializer
    permission_classes = [permissions.IsAdminUser] 
    authentication_classes = [TokenAuthentication]
    

    def get_queryset(self):
        vacancy_id = self.kwargs['pk']
        return VacancyRequest.objects.filter(vacancy_id=vacancy_id)