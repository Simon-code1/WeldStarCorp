from django.urls import path
from . import views
app_name = 'base'

urlpatterns =[
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('services/', views.services, name="services"),
    path('projects/', views.projects, name="projects"),
    path('<slug:slug>/', views.project_detail, name='project_detail'),
    path('contact_us', views.contact_us, name="contact_us")
]