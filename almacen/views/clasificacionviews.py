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

class ClasificacionesListView(LoginRequiredMixin,ListView):
    model = Clasificaciones
    template_name = 'clasificacion/index.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = _('clasification_list_header')
        context['form'] = ClasificacionesForm()
        return context

class ClasificacionesCreateView(PermissionRequiredMixin,LoginRequiredMixin,SuccessMessageMixin, CreateView):
    permission_required = 'almacen.add_clasificaciones'
    model = Clasificaciones
    form_class = ClasificacionesForm
    # template_name = 'clasificacion/index.html'
    success_url = reverse_lazy('clasificaciones')
    # success_message = _('success_insert')
    def dispatch(self, request, *args, **kwargs):
        if request.user.has_perm('almacen.add_clasificaciones'):           
            return super().dispatch(request, *args, **kwargs)
        else:
            messages.error(self.request, _('No_authorized'))
            return redirect('clasificaciones')

    def form_valid(self, form):
      messages.success(self.request, _('success_insert_clasification'))
      return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) 
        return context

class ClasificacionesUpdateView(PermissionRequiredMixin,LoginRequiredMixin,SuccessMessageMixin, UpdateView):
    permission_required = 'almacen.change_clasificaciones'
    model = Clasificaciones
    form_class = ClasificacionesForm
    template_name = 'clasificacion/edit.html'
    success_url = reverse_lazy('clasificaciones')
    # success_message = _('success_update')
    def dispatch(self, request, *args, **kwargs):
        if request.user.has_perm('almacen.change_clasificaciones'):           
            return super().dispatch(request, *args, **kwargs)
        else:
            messages.error(self.request, _('No_authorized'))
            return redirect('clasificaciones')
    def form_valid(self, form):
      messages.success(self.request, _('success_update_clasification'))
      return super().form_valid(form)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) 
        return context

class ClasificacionesDeleteView(PermissionRequiredMixin,LoginRequiredMixin,SuccessMessageMixin, DeleteView):
    permission_required = 'almacen.delete_clasificaciones'
    model = Clasificaciones
    success_url = reverse_lazy('clasificaciones')
    success_message = _('success_delete')
    def dispatch(self, request, *args, **kwargs):
        if request.user.has_perm('almacen.delete_clasificaciones'):           
            return super().dispatch(request, *args, **kwargs)
        else:
            messages.error(self.request, _('No_authorized'))
            return redirect('clasificaciones')
    def form_valid(self, form):
      messages.success(self.request, _('success_delete_clasification'))
      return super().form_valid(form)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) 
        return context
