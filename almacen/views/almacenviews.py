from datetime import datetime
from multiprocessing import context
from pyexpat import model
from pyexpat.errors import messages
from typing import final
from urllib import request
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpRequest
from almacen.models import Almacen, Almacenmercancia, Clasificaciones, Mercancia, Recepcion, Recepcionmercancias
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.views.generic import ListView, CreateView,DeleteView,UpdateView,TemplateView, FormView
from django.utils.decorators import method_decorator
from almacen.forms import AlmacenesForm, ClasificacionesForm,  MercanciasForm, RecepcionForm, AddRecepcionmercanciaForm,EditRecepcionmercanciaForm
from django.urls import reverse_lazy,reverse
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import ModelFormMixin
from django.shortcuts import get_object_or_404,redirect
from django.contrib import messages
from django.utils.translation import gettext as _
from django.contrib.auth.decorators import login_required,permission_required
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin

class AlmacenesListView(LoginRequiredMixin,ListView):
    model = Almacen
    template_name = 'almacen/index.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = _('Store_List_Header')
        context['form'] = AlmacenesForm
        return context

class AlmacenesCreateView(PermissionRequiredMixin,LoginRequiredMixin,SuccessMessageMixin, CreateView):
    permission_required = 'almacen.add_almacen'
    model = Almacen
    form_class = AlmacenesForm
    success_url = reverse_lazy('almacenes')
    def form_valid(self, form):
      messages.success(self.request, _('success_insert_store'))
      return super().form_valid(form)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) 
        return context
    def dispatch(self, request, *args, **kwargs):
        if request.user.has_perm('almacen.add_almacen'):           
            return super().dispatch(request, *args, **kwargs)
        else:
            messages.error(self.request, _('No_authorized'))
            return redirect('almacenes')

class AlmacenesUpdateView(PermissionRequiredMixin,LoginRequiredMixin,SuccessMessageMixin, UpdateView):
    permission_required = 'almacen.change_almacen'
    model = Almacen
    form_class = AlmacenesForm
    template_name = 'almacen/edit.html'
    success_url = reverse_lazy('almacenes')
    def dispatch(self, request, *args, **kwargs):
        if request.user.has_perm('almacen.change_almacen'):           
            return super().dispatch(request, *args, **kwargs)
        else:
            messages.error(self.request, _('No_authorized'))
            return redirect('almacenes')
    def form_valid(self, form):
      messages.success(self.request, _('success_udpate_store'))
      return super().form_valid(form)    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) 
        almacenmercancias = Almacenmercancia.objects.filter(almacen=self.object)
        recepciones = Recepcion.objects.filter(almacen=self.object)
        context['almacenmercancias'] = almacenmercancias
        context['formRecepcion'] = RecepcionForm
        context['recepciones'] = recepciones
        context['almacen'] = self.object
        return context
    
class AlmacenesDeleteView(PermissionRequiredMixin,LoginRequiredMixin,SuccessMessageMixin, DeleteView):
    permission_required = 'almacen.delete_almacen'
    model = Almacen
    success_url = reverse_lazy('almacenes')
    # success_message = _('success_delete')
    def dispatch(self, request, *args, **kwargs):
        if request.user.has_perm('almacen.delete_almacen'):           
            return super().dispatch(request, *args, **kwargs)
        else:
            messages.error(self.request, _('No_authorized'))
            return redirect('almacenes')
    def form_valid(self, form):
      messages.success(self.request, _('success_delete_store'))
      return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) 
        return context
