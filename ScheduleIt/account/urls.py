from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required

from .views import *
from . import views



urlpatterns = [
    #path('login/', views.user_login, name='login') ---->>> modelo crado por nosotros

    # Modelos que vienen por defecto en Django
    #path('login/', auth_views.LoginView.as_view(), name='login'),
    #path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    #path('password-change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    #path('password-change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('', include('django.contrib.auth.urls')),
    path('', login_required(Dashboard.as_view()), name='dashboard'),
    path('register/', views.register, name='register'),
    path('calendar/', login_required(EventosCalendario.as_view()), name='calendar'),
    path('settings/', login_required(SettingsView.as_view()), name='settings'),
    path('calendar/evaluacion_create/', login_required(EvaluacionCreateView.as_view()), name='evaluacion_create'),
    path('calendar/evaluacion_update/<int:pk>/', login_required(EvaluacionUpdateView.as_view()), name='evaluacion_update'),
    path('calendar/evaluacion_delete/<int:pk>/', login_required(EvaluacionDeleteView.as_view()), name='evaluacion_delete'),
    path('calendar/evaluacion_detail/<int:pk>/', login_required(EvaluacionDetailView.as_view()), name='evaluacion_detail'),
    path('home/', home.as_view(), name='home'),
]