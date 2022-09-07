from multiprocessing import context
from pyexpat import model
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpRequest
from almacen.models import Almacen, Clasificaciones, Mercancia
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.views.generic import ListView, CreateView,DeleteView,UpdateView,TemplateView, FormView
# from django.http import JsonResponse
from django.utils.decorators import method_decorator
from almacen.forms import AlmacenesForm, ClasificacionesForm, MercanciasForm
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
# from django.shortcuts import get_object_or_404


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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) 
        return context

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