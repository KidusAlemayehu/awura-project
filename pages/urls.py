from django.urls import path
from. import views
urlpatterns = [
    path('',views.landing, name='landing'),
    path('services',views.services, name='services'),
    path('projects',views.projects, name='projects'),
    path('vacancy', views.vacancy, name='vacancy'),
    path('contact',views.contact, name='contact'),
]
