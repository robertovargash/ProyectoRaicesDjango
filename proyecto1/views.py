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