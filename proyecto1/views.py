from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.generic import ListView, CreateView,DeleteView,UpdateView,TemplateView, FormView
from django.utils.translation import gettext as _
from django.contrib import messages
from django.urls import reverse_lazy,reverse
from proyecto1.forms import *
from django.shortcuts import get_object_or_404,redirect


class UserListView(ListView):
    model = User
    template_name = 'auth/index.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = _('user_list_header')
        context['fromUser'] = AddUserForm
        return context

class UserCreateView(CreateView):
    model = User
    form_class = AddUserForm
    success_url = reverse_lazy('users')
    # success_message = _('success_insert')

    def form_valid(self, form):
        self.object = form.save()
        # almacenes = Almacen.objects.all()
        messages.success(self.request, _('success_insert_user'))
        # for almacen in almacenes:
        #     almacenmercancia = Almacenmercancia()
        #     almacenmercancia.almacen = almacen
        #     almacenmercancia.mercancia = self.object
        #     almacenmercancia.cantidad = 0            
        #     almacenmercancia.save()
        return super().form_valid(form)

class UserUpdateView(UpdateView):
    model = User
    template_name = 'auth/edit.html'
    form_class = EditUserForm
    success_url = reverse_lazy('users')
    # success_message = _('success_insert')

    def form_valid(self, form):
        self.object = form.save()
        # almacenes = Almacen.objects.all()
        messages.success(self.request, _('success_update_user'))
        # for almacen in almacenes:
        #     almacenmercancia = Almacenmercancia()
        #     almacenmercancia.almacen = almacen
        #     almacenmercancia.mercancia = self.object
        #     almacenmercancia.cantidad = 0            
        #     almacenmercancia.save()
        return super().form_valid(form)

def disable_user(request, pk):
    user = User.objects.get(pk=pk)
    
    if user.is_active == True:
        user.is_active = False       
        user.save()
        messages.add_message(request, messages.SUCCESS, _('success_disable_user'))
        return redirect('users')
    else:
        messages.add_message(request, messages.ERROR, _('error_disable_user'))
        return redirect('users')

def enable_user(request, pk):
    user = User.objects.get(pk=pk)    
    if user.is_active == False:
        user.is_active = True       
        user.save()
        messages.add_message(request, messages.SUCCESS, _('success_enable_user'))
        return redirect('users')
    else:
        messages.add_message(request, messages.ERROR, _('error_enable_user'))
        return redirect('users')