from django.urls import path
from .views import( VacancyListCreateView, VacancyRetrieveUpdateDeleteView,VacancyRequestCreateView,
    VacancyRequestListView,AdminLoginView)

urlpatterns = [
    path('vacancies/', VacancyListCreateView.as_view(), name='vacancy-list'),
    path('vacancies/<int:pk>/', VacancyRetrieveUpdateDeleteView.as_view(), name='vacancy-detail'),
    path('vacancies/<int:pk>/requests/', VacancyRequestListView.as_view(), name='vacancy-request-list'),
    path('vacancy-requests/', VacancyRequestCreateView.as_view(), name='vacancy-request-create'),
    path('login/', AdminLoginView.as_view(), name='admin-login'),
]