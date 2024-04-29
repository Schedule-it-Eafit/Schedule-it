from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.views.generic import View, ListView, TemplateView, CreateView, UpdateView, DeleteView
from django.http import HttpResponse

from .forms import LoginForm, UserRegistrationForm
from .models import Evaluacion
from django.contrib.auth.models import User
from django.urls import reverse_lazy

# Create your views here.

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,
                                username=cd['username'],
                                password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Usuario autenticado')
                else:
                    return HttpResponse('Usuario no activo')
            else:
                return HttpResponse('Usuario o contraseña incorrectos')
    else:
        form = LoginForm()
        return render(request, 'account/login.html', {'form': form})

class Dashboard(TemplateView):
    template_name = 'account/dashboard.html'
    

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return render(request, 
                          'account/register_done.html', 
                          {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
        return render(request, 
                      'account/register.html', 
                      {'user_form': user_form})


class EventosCalendario(ListView):
    model = Evaluacion
    template_name = 'account/calendar.html'

    def get_queryset(self):
        return Evaluacion.objects.filter(usuario=self.request.user)
    

class SettingsView(TemplateView):
    template_name = 'account/settings.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context
    

class EvaluacionCreateView(CreateView):
    model = Evaluacion
    template_name = 'account/evaluacion_create.html'
    fields = ('nombre', 'materia', 'fecha', 'hora', 'hora_fin', 'lugar', 'descripcion', 'color',)

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)
    
    success_url = reverse_lazy('calendar')


class EvaluacionUpdateView(UpdateView):
    model = Evaluacion
    template_name = 'account/evaluacion_update.html'
    fields = ('nombre', 'materia', 'fecha', 'hora', 'hora_fin', 'lugar', 'descripcion', 'color',)
    
    success_url = reverse_lazy('calendar')


class EvaluacionDeleteView(DeleteView):
    model = Evaluacion
    template_name = 'account/evaluacion_delete.html'
    
    success_url = reverse_lazy('calendar')