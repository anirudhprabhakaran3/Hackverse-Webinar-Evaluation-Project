from django.urls import path
from submissions import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('submissions/<int:pk>', views.view_submission, name='view_submission'),
    path('submissions/add', views.add_submission, name='add_submission'),
    path('submissions/add/<int:pk>', views.add_marks, name='add_marks'),
    path('scoreboard', views.scoreboard, name='scoreboard'),
    
    path('login', auth_views.LoginView.as_view(), name='login'),
    path('logout', auth_views.LogoutView.as_view(), name='logout'),
    path('register', views.register, name='register'),
]