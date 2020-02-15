from django.urls import path
from sadat import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'), 
    path('projects/', views.projects),   
    path('tutorial/', views.tutorial),
    # path('form_page/', views.form_page),
    # path('user_signup_form/', views.user_signup_form),
    # path('user_registration_form/', views.user_registration_form),
    # path('', views.home.as_view(), name='home')    
]
