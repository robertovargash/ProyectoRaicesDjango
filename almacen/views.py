from datetime import datetime
from multiprocessing import context
from pyexpat import model
from pyexpat.errors import messages
from urllib import request
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpRequest
from almacen.models import Almacen, Almacenmercancia, Clasificaciones, Mercancia, Recepcion
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.views.generic import ListView, CreateView,DeleteView,UpdateView,TemplateView, FormView
# from django.http import JsonResponse
from django.utils.decorators import method_decorator
from almacen.forms import AddRecepcionForm, AlmacenesForm, ClasificacionesForm, EditRecepcionForm, MercanciasForm, RecepcionForm
from django.urls import reverse_lazy,reverse
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import ModelFormMixin
from django.shortcuts import get_object_or_404,redirect
from django.contrib import messages
from django.http import JsonResponse


# Create your views here.
# def almacenes(request):
#     """Renders the home page."""
#     assert isinstance(request, HttpRequest)
#     data = {
#         'title': "Lista Almacenes",
#         'almacenes' : Almacen.objects.all()
#     }
#     return render(
#         request,
#         'pages/index.html',data
#     )

class AlmacenesListView(ListView):
    model = Almacen
    template_name = 'almacen/index.html'
    success_message = "Bien!!!!"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Lista de Almacenes"
        context['form'] = AlmacenesForm
        return context

class AlmacenesCreateView(SuccessMessageMixin, CreateView):
    model = Almacen
    form_class = AlmacenesForm
    success_url = reverse_lazy('almacenes')
    success_message = "Insertado correctamente!!!!"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) 
        return context

class AlmacenesUpdateView(SuccessMessageMixin, UpdateView):
    model = Almacen
    form_class = AlmacenesForm
    template_name = 'almacen/edit.html'
    success_url = reverse_lazy('almacenes')
    success_message = "Actualizado correctamente!!!!"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) 
        almacenmercancias = Almacenmercancia.objects.filter(almacen=self.object)
        recepciones = Recepcion.objects.filter(almacen=self.object)
        context['almacenmercancias'] = almacenmercancias
        context['formRecepcion'] = RecepcionForm
        context['recepciones'] = recepciones
        context['almacen'] = self.object
        return context
    
class AlmacenesDeleteView(SuccessMessageMixin, DeleteView):
    model = Almacen
    success_url = reverse_lazy('almacenes')
    success_message = "Eliminado correctamente!!!!"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) 
        return context


class MercanciasListView(ListView):
    model = Mercancia
    template_name = 'mercancia/index.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Lista de mercancias"
        context['form'] = MercanciasForm
        return context

class MercanciasCreateView(SuccessMessageMixin, CreateView):
    model = Mercancia
    form_class = MercanciasForm
    success_url = reverse_lazy('mercancias')
    success_message = "Insertado correctamente!!!!"
    def form_valid(self, form):
        self.object = form.save()
        almacenes = Almacen.objects.all()
        for almacen in almacenes:
            almacenmercancia = Almacenmercancia()
            almacenmercancia.almacen = almacen
            almacenmercancia.mercancia = self.object
            almacenmercancia.cantidad = 0            
            almacenmercancia.save()
        return super().form_valid(form)
    # def form_valid(self, form):
    #     # self.object = form.save(commit=False)
    #     almacenes = Almacen.objects.all()
    #     for almacen in almacenes:
    #         almacenmercancia = Almacenmercancia()
    #         almacenmercancia.almacen = almacen
    #         almacenmercancia.cantidad - 0
    #         almacenmercancia.mercancia = self.object
    #         almacenmercancia.save()
        # for person in form.cleaned_data['members']:
        #     membership = Membership()
        #     membership.group = self.object
        #     membership.person = person
        #     membership.save()
        # return super(ModelFormMixin, self).form_valid(form)

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     return context

class MercanciasUpdateView(SuccessMessageMixin, UpdateView):
    model = Mercancia
    form_class = MercanciasForm
    template_name = 'mercancia/edit.html'
    success_url = reverse_lazy('mercancias')
    success_message = "Actualizado correctamente!!!!"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class MercanciasDeleteView(SuccessMessageMixin, DeleteView):
    model = Mercancia
    success_url = reverse_lazy('mercancias')
    success_message = "Eliminado correctamente!!!!"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) 
        return context

class ClasificacionesListView(ListView):
    model = Clasificaciones
    template_name = 'clasificacion/index.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Lista de clasificaciones"
        context['form'] = ClasificacionesForm()
        return context

class ClasificacionesCreateView(SuccessMessageMixin, CreateView):
    model = Clasificaciones
    form_class = ClasificacionesForm
    # template_name = 'clasificacion/index.html'
    success_url = reverse_lazy('clasificaciones')
    success_message = "Insertado correctamente!!!!"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) 
        return context

class ClasificacionesUpdateView(SuccessMessageMixin, UpdateView):
    model = Clasificaciones
    form_class = ClasificacionesForm
    template_name = 'clasificacion/edit.html'
    success_url = reverse_lazy('clasificaciones')
    success_message = "Actualizado correctamente!!!!"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) 
        return context

class ClasificacionesDeleteView(SuccessMessageMixin, DeleteView):
    model = Clasificaciones
    success_url = reverse_lazy('clasificaciones')
    success_message = "Eliminado correctamente!!!!"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) 
        return context

class RecepcionCreateView(SuccessMessageMixin, CreateView):
    model = Recepcion
    form_class = RecepcionForm
    # path('almacenes/<int:pk>/update/', AlmacenesUpdateView.as_view(), name='editar_almacen'),
    # success_url = reverse_lazy('almacenes')
    success_message = "Insertado correctamente!!!!"
    def form_valid(self, form):
        count = Recepcion.objects.all().count()
        self.object = form.save(commit=False)
        self.object.fecha = datetime.now()        
        self.object.activo = 0
        self.object.almacen_id = self.request.POST['almacenid']
        self.object.numero = count+1
        self.object.save()         
        print(self.request)
        return redirect('editar_recepcion', pk=self.object.id)

class RecepcionUpdateView(SuccessMessageMixin, UpdateView):
    model = Recepcion
    form_class = RecepcionForm
    template_name = 'recepcion/edit.html'
    # success_url = reverse_lazy('almacenes')
    success_message = "Actualizado correctamente!!!!"
    def form_valid(self, form):
        self.object = form.save(commit=False)
        # self.object.numero = 0
        # self.object.fecha = datetime.now()
        # self.object.activo = 1
        # self.object.almacen_id = 42
        self.object.save() 
        return redirect('editar_almacen', pk=self.object.almacen_id)
    
    # def form_valid(self, form):
    #     self.object = form.save(commit=False)
    #     self.object.numero = 0
    #     self.object.fecha = datetime.now()
    #     self.object.activo = 1
    #     self.object.almacen = self.request.almacen_id
    #     self.object.save() 
    #     self.fields['numero'].numero = 0
    #     self.fields['fecha'] = datetime.now()
    #     self.fields['activo'] = 1
    #     self.fields['almacen_id'] = 42
    #     self.object = form.save()
    #     return super().form_valid(form)
    # def form_valid(self, form):
    #     self.object = form.save()
    #     almacenes = Almacen.objects.all()
    #     for almacen in almacenes:
    #         almacenmercancia = Almacenmercancia()
    #         almacenmercancia.almacen = almacen
    #         almacenmercancia.mercancia = self.object
    #         almacenmercancia.cantidad = 0            
    #         almacenmercancia.save()
    #     return super().form_valid(form)

def cancelar_recepcion(request, pk):
    recepcion = Recepcion.objects.get(pk=pk)
    recepcion.activo = 2
    recepcion.save()
    return redirect(reverse('editar_almacen', kwargs={"pk": recepcion.almacen_id}))

def firmar_recepcion(request, pk):
    recepcion = Recepcion.objects.get(pk=pk)
    recepcion.activo = 1
    recepcion.save()
    return redirect(reverse('editar_almacen', kwargs={"pk": recepcion.almacen_id}))

def add_recepcion_view(request):
    print("add recepcion")
    if request.POST:
        almacen_id = request.POST['almacen_id']
        numero = request.POST['numero']
        observaciones = request.POST['observaciones']
        precibe = request.POST['precibe']
        pentrega = request.POST['pentrega']
        pautoriza = request.POST['pautoriza']
        contrato = request.POST['contrato']
        factura = request.POST['factura']
        proveedor = request.POST['proveedor']
        recepcion = Recepcion.objects.create(
            almacen_id = almacen_id,
            numero = numero,
            observaciones = observaciones,
            precibe = precibe,
            pentrega = pentrega,
            pautoriza = pautoriza,
            contrato = contrato,
            factura = factura,
            proveedor = proveedor,
            fecha = datetime.now(),
            activo = 1
        )
        messages.success(request, 'Profile details updated.')
        return redirect(reverse('editar_recepcion', kwargs={"pk": recepcion.id}))
        # return redirect(resolve_url(to, *args, **kwargs)reverse_lazy('editar_almacen',42))
        # form = AddRecepcionForm(request.POST, request.FILES)
        # if form.is_valid:
        #     try:
        #         form.save()
        #     except:
        #         messages(request,"Error al add recepcion")
        #         return redirect('almacenes')
    return redirect(reverse('editar_recepcion', kwargs={"pk": recepcion.id}))

def edit_recepcion_view(request, pk):
    recepcion =Recepcion.objects.get(pk=pk)
    edit_form = EditRecepcionForm()
    print(recepcion)
    # return redirect('almacenes')
    return render(request,"recepcion/edit.html",{'recepcion':recepcion,'almacenid':recepcion.almacen_id,'edit_form':edit_form})

def edit_recepcion(request):
    recepcion = Recepcion.objects.get(pk=request.POST['id'])
    recepcion.observaciones = request.POST['observaciones']
    recepcion.precibe = request.POST['precibe']
    recepcion.pentrega = request.POST['pentrega']
    recepcion.pautoriza = request.POST['pautoriza']
    recepcion.contrato = request.POST['contrato']
    recepcion.factura = request.POST['factura']
    recepcion.proveedor = request.POST['proveedor']
    recepcion.save()
    return redirect(reverse('editar_almacen', kwargs={"pk": recepcion.almacen_id}))
    # return render(request,"recepcion/edit.html",{"recepcion":recepcion,"edit_form":edit_form})


def delete_recepcion_view(request):
    
    return redirect('almacenes')