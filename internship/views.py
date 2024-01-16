from rest_framework import generics,permissions
from .models import InternshipRole, InternshipRequest
from .serializers import InternshipRoleSerializer, InternshipRequestSerializer

class InternshipRoleListCreateAPIView(generics.ListCreateAPIView):
    queryset = InternshipRole.objects.all()
    serializer_class = InternshipRoleSerializer
    permission_classes=[permissions.IsAuthenticatedOrReadOnly]
    
    def perform_create(self, serializer):
        if not self.request.user.is_staff:
            raise PermissionError("only admin can create vacancy posts")
        serializer.save()
    

class InternshipRequestListCreateAPIView(generics.ListCreateAPIView):
    queryset = InternshipRequest.objects.all()
    serializer_class = InternshipRequestSerializer
    permission_classes=[permissions.AllowAny]


class InternshipRequestListView(generics.ListAPIView):
    serializer_class = InternshipRequestSerializer
    permission_classes = [permissions.IsAdminUser]

    def get_queryset(self):
        internship_id = self.kwargs['pk']
        return InternshipRequest.objects.filter(internship_id=internship_id)