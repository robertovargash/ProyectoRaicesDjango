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
# from django.http import JsonResponse
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

class RecepcionCreateView(PermissionRequiredMixin,LoginRequiredMixin,SuccessMessageMixin, CreateView):
    permission_required = 'almacen.add_recepcion'
    model = Recepcion
    form_class = RecepcionForm
    def form_valid(self, form):
        count = Recepcion.objects.all().count()
        self.object = form.save(commit=False)
        self.object.fecha = datetime.now()        
        self.object.activo = 0
        self.object.almacen_id = self.request.POST['almacenid']
        self.object.numero = count+1
        self.object.save()
        messages.success(self.request, _('success_insert_reception'))
        return redirect('editar_recepcion', pk=self.object.id)
    def dispatch(self, request, *args, **kwargs):
        if request.user.has_perm('almacen.add_recepcion'):           
            return super().dispatch(request, *args, **kwargs)
        else:
            messages.error(self.request, _('No_authorized'))
            return redirect('editar_almacen', self.request.POST['almacenid'])

class RecepcionUpdateView(PermissionRequiredMixin,LoginRequiredMixin,SuccessMessageMixin, UpdateView):
    permission_required = 'almacen.change_recepcion'
    model = Recepcion
    form_class = RecepcionForm
    template_name = 'recepcion/edit.html'
    # success_url = reverse_lazy('almacenes')
    # success_message = _('success_update')
    def dispatch(self, request, *args, **kwargs):
        if request.user.has_perm('almacen.change_recepcion'):           
            return super().dispatch(request, *args, **kwargs)
        else:
            messages.error(self.request, _('No_authorized'))
            return redirect('editar_almacen', self.request.POST['almacenid'])
    def get_success_url(self):
        almacen_id = self.object.almacen_id 
        return reverse( 'editar_almacen', kwargs={'pk': almacen_id})
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save() 
        messages.success(self.request, _('success_update_reception'))
        return super(RecepcionUpdateView, self).form_valid(form)
        # return redirect('editar_almacen', pk=self.object.almacen_id)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) 
        formadd = AddRecepcionmercanciaForm()
        recepcionmerc = Recepcionmercancias.objects.filter(recepcion=self.object).values('mercancia_id')
        mercancias = Mercancia.objects.exclude(id__in=recepcionmerc)
        formadd.fields['mercancia'].queryset = mercancias
        context['formAddRecepcion'] = formadd
        context['mercancias'] = mercancias
        context['formEditRecepcion'] = EditRecepcionmercanciaForm()
        context['recepcionmercancias'] = Recepcionmercancias.objects.filter(recepcion=self.object)
        return context

@login_required(login_url='/accounts/login/')
def cancelar_recepcion(request, pk):
    recepcion = Recepcion.objects.get(pk=pk)
    if recepcion.activo == 0:
        recepcion.activo = 2
        recepcion.save()
        mess = _('success_cancel_reception')
        messages.add_message(request, messages.SUCCESS, mess)
        return redirect(reverse('editar_almacen', kwargs={"pk": recepcion.almacen_id}) + '#cardRecepciones')
    else:
        mess = _('error_cancel_reception')
        messages.add_message(request, messages.ERROR, mess)
        return redirect(reverse('editar_almacen', kwargs={"pk": recepcion.almacen_id}) + '#cardRecepciones')

@login_required(login_url='/accounts/login/')
def firmar_recepcion(request, pk):
    recepcion = Recepcion.objects.get(pk=pk)
    recepcionesmercancias = Recepcionmercancias.objects.filter(recepcion_id=recepcion.id)
    if recepcion.activo == 0:
        recepcion.activo = 1
        for recepmerc in recepcionesmercancias:
            almacenmercancia = Almacenmercancia.objects.filter(mercancia_id = recepmerc.mercancia_id).filter(almacen_id = recepcion.almacen_id).first()
            cantidad1 = almacenmercancia.cantidad
            almacenmercancia.cantidad = almacenmercancia.cantidad + recepmerc.cantidad
            mercancia = Mercancia.objects.get(pk=almacenmercancia.mercancia_id)
            precio1 = mercancia.precio
            mercancia.precio = ((precio1*cantidad1) +  (recepmerc.precio*recepmerc.cantidad))/(cantidad1 + recepmerc.cantidad)
            almacenmercancia.save()
            mercancia.save()
        recepcion.save()
        messages.add_message(request, messages.SUCCESS, _('success_sign_reception'))
        return redirect(reverse('editar_almacen', kwargs={"pk": recepcion.almacen_id}) + '#cardRecepciones')
    else:
        messages.add_message(request, messages.ERROR, _('error_sign_reception'))
        return redirect(reverse('editar_almacen', kwargs={"pk": recepcion.almacen_id}) + '#cardRecepciones')
    
class RecepcionmercanciaCreateView(PermissionRequiredMixin,LoginRequiredMixin,SuccessMessageMixin, CreateView):
    permission_required = 'almacen.add_recepcionmercancias'
    model = Recepcionmercancias
    form_class = AddRecepcionmercanciaForm
    # path('almacenes/<int:pk>/update/', AlmacenesUpdateView.as_view(), name='editar_almacen'),
    # success_url = reverse_lazy('almacenes')
    # success_message = _('success_insert')
    def get_success_url(self):
        recepcion_id = self.object.recepcion_id 
        return reverse( 'editar_recepcion', kwargs={'pk': recepcion_id})
    def form_valid(self, form):
        # count = Recepcion.objects.all().count()
        self.object = form.save(commit=False)
        self.object.recepcion_id = self.request.POST['recepcion_id']
        self.object.save()
        messages.success(self.request, _('success_insert_receptionproduct'))
        return super(RecepcionmercanciaCreateView, self).form_valid(form)
    def dispatch(self, request, *args, **kwargs):
        if request.user.has_perm('almacen.add_recepcionmercancias'):           
            return super().dispatch(request, *args, **kwargs)
        else:
            messages.error(self.request, _('No_authorized'))
            return redirect('editar_recepcion', self.request.POST['recepcion_id'])

class RecepcionmercanciaDeleteView(PermissionRequiredMixin,LoginRequiredMixin,SuccessMessageMixin, DeleteView):
    permission_required = 'almacen.delete_recepcionmercancias'
    model = Recepcionmercancias
    def dispatch(self, request, *args, **kwargs):
        if request.user.has_perm('almacen.delete_recepcionmercancias'):           
            return super().dispatch(request, *args, **kwargs)
        else:
            messages.error(self.request, _('No_authorized'))
            return redirect('editar_recepcion', self.request.POST['recepcion_id'])
    # success_message = _('success_delete')
    def form_valid(self, form):
      messages.success(self.request, _('success_delete_receptionproduct'))
      return super().form_valid(form)
    def get_success_url(self):
        recepcion_id = self.object.recepcion_id 
        return reverse( 'editar_recepcion', kwargs={'pk': recepcion_id})

class RecepcionmercanciaUpdateView(PermissionRequiredMixin,LoginRequiredMixin,SuccessMessageMixin, UpdateView):
    permission_required = 'almacen.change_recepcionmercancias'
    model = Recepcionmercancias
    form_class = EditRecepcionmercanciaForm
    # path('almacenes/<int:pk>/update/', AlmacenesUpdateView.as_view(), name='editar_almacen'),
    # success_url = reverse_lazy('almacenes')
    # success_message = _('success_udpate')
    def form_valid(self, form):
      messages.success(self.request, _('success_udpate_receptionproduct'))
      return super().form_valid(form)
    def get_success_url(self):
        recepcion_id = self.object.recepcion_id 
        return reverse( 'editar_recepcion', kwargs={'pk': recepcion_id})
    def dispatch(self, request, *args, **kwargs):
        if request.user.has_perm('almacen.change_recepcionmercancias'):           
            return super().dispatch(request, *args, **kwargs)
        else:
            messages.error(self.request, _('No_authorized'))
            return redirect('editar_recepcion', self.request.POST['recepcion_id'])

        
    # def delete(self, *args, **kwargs):
    #     # self.object = self.get_object()
    #     # recep = Recepcion.objects.get(pk=self.object.recepcion_id)
    #     return super(RecepcionmercanciaDeleteView, self).delete(*args, **kwargs)
        # return redirect('editar_recepcion', pk=recep.id)
    # def form_valid(self, form):
    #     self.object = form.save(commit=False)
    #     recep = Recepcion.objects.get(pk=self.object.recepcion_id)
    #     recepmercancia = Recepcionmercancias.objects.get(pk=self.object.id)
    #     recepmercancia.delete()
    #     return redirect('editar_recepcion', pk=recep.id)