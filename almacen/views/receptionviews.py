
from datetime import datetime
from pyexpat.errors import messages
from django.shortcuts import render
from almacen.models import Almacen, Almacenmercancia, Mercancia, Recepcion, Recepcionmercancias
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.views.generic import ListView, CreateView,DeleteView,UpdateView
from django.utils.decorators import method_decorator
from almacen.forms import RecepcionForm, AddRecepcionmercanciaForm,EditRecepcionmercanciaForm
from django.urls import reverse_lazy,reverse
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import get_object_or_404,redirect
from django.contrib import messages
from django.utils.translation import gettext as _
from django.contrib.auth.decorators import login_required,permission_required
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin

class RecepcionCreateView(PermissionRequiredMixin,LoginRequiredMixin,SuccessMessageMixin, CreateView):
    permission_required = 'almacen.add_recepcion'
    model = Recepcion
    form_class = RecepcionForm
   
    def form_valid(self, form):
        count = Recepcion.objects.all().count()        
        self.object = form.save(commit=False)
        self.object.fecha = datetime.now()
        self.object.precibe = self.request.user
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
@permission_required('almacen.cancel_recepcion')
def cancelar_recepcion(request, pk):
    recepcion = Recepcion.objects.get(pk=pk)
    if recepcion.activo == 0:
        recepcion.activo = 2
        recepcion.pautoriza = "Nobody, Cancelled"
        recepcion.save()
        mess = _('success_cancel_reception')
        messages.add_message(request, messages.SUCCESS, mess)
        return redirect(reverse('editar_almacen', kwargs={"pk": recepcion.almacen_id}) + '#cardRecepciones')
    else:
        mess = _('error_cancel_reception')
        messages.add_message(request, messages.ERROR, mess)
        return redirect(reverse('editar_almacen', kwargs={"pk": recepcion.almacen_id}) + '#cardRecepciones')

@login_required(login_url='/accounts/login/')
@permission_required('almacen.sign_recepcion')
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
        recepcion.pautoriza = request.user.first_name + " " + request.user.last_name
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
