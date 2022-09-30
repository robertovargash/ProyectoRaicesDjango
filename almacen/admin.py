from django.contrib import admin
from django.contrib.auth.models import Permission

from almacen.models import Almacen,Recepcion,Mercancia,Clasificaciones,Recepcionmercancias,Almacenmercancia,Vale,Valeitems
# Register your models here.
admin.site.register(Almacen)
admin.site.register(Recepcion)
admin.site.register(Mercancia)
admin.site.register(Clasificaciones)
admin.site.register(Recepcionmercancias)
admin.site.register(Almacenmercancia)
admin.site.register(Vale)
admin.site.register(Permission)