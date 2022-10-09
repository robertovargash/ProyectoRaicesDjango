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

class MercanciasListView(LoginRequiredMixin,ListView):
    model = Mercancia
    template_name = 'mercancia/index.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = _('Product_List_Header')
        context['form'] = MercanciasForm
        return context

class MercanciasCreateView(PermissionRequiredMixin,LoginRequiredMixin,SuccessMessageMixin, CreateView):
    permission_required = 'almacen.add_mercancia'
    model = Mercancia
    form_class = MercanciasForm
    success_url = reverse_lazy('mercancias')
    # success_message = _('success_insert')
    def dispatch(self, request, *args, **kwargs):
        if request.user.has_perm('almacen.add_mercancia'):           
            return super().dispatch(request, *args, **kwargs)
        else:
            messages.error(self.request, _('No_authorized'))
            return redirect('mercancias')
    def form_valid(self, form):
        self.object = form.save()
        almacenes = Almacen.objects.all()
        messages.success(self.request, _('success_insert_product'))
        for almacen in almacenes:
            almacenmercancia = Almacenmercancia()
            almacenmercancia.almacen = almacen
            almacenmercancia.mercancia = self.object
            almacenmercancia.cantidad = 0            
            almacenmercancia.save()
        return super().form_valid(form)

class MercanciasUpdateView(PermissionRequiredMixin,LoginRequiredMixin,SuccessMessageMixin, UpdateView):
    permission_required = 'almacen.change_mercancia'
    model = Mercancia
    form_class = MercanciasForm
    template_name = 'mercancia/edit.html'
    success_url = reverse_lazy('mercancias')
    # success_message = _('success_udpate')

    def form_valid(self, form):
      messages.success(self.request, _('success_udpate_product'))
      return super().form_valid(form)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    def dispatch(self, request, *args, **kwargs):
        if request.user.has_perm('almacen.change_mercancia'):           
            return super().dispatch(request, *args, **kwargs)
        else:
            messages.error(self.request, _('No_authorized'))
            return redirect('mercancias')

class MercanciasDeleteView(PermissionRequiredMixin,LoginRequiredMixin,SuccessMessageMixin, DeleteView):
    permission_required = 'almacen.delete_mercancia'
    model = Mercancia
    success_url = reverse_lazy('mercancias')
    # success_message = _('success_delete')
    def form_valid(self, form):
      messages.success(self.request, _('success_delete_product'))
      return super().form_valid(form)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) 
        return context
    def dispatch(self, request, *args, **kwargs):
        if request.user.has_perm('almacen.delete_mercancia'):           
            return super().dispatch(request, *args, **kwargs)
        else:
            messages.error(self.request, _('No_authorized'))
            return redirect('mercancias')    
