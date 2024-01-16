
from django.urls import path
from .views import (
    InternshipRoleListCreateAPIView,
    InternshipRequestListCreateAPIView,
    InternshipRequestListView,
)



urlpatterns = [
    path('api/internship/roles/', InternshipRoleListCreateAPIView.as_view(), name='internship_role_list_create_api'),
    path('api/internship/requests/', InternshipRequestListCreateAPIView.as_view(), name='internship_request_list_create_api'),
    path('api/internship/requests/<int:pk>/', InternshipRequestListView.as_view(), name='internship_request_retrieve_update_destroy_api'),
]