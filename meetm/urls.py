from django.urls import path
from . import views


urlpatterns = [
    path('', views.home , name='home' ),
    path('user_home/', views.user_home , name='userhome') ,
    path('moderator_home/', views.moderator_home , name='moderatorhome') ,
    path('user_signup/', views.user_signup , name='usersignup') ,
    path('moderator_home/plan_meeting/', views.plan_meeting , name='planmeeting') ,
    ]