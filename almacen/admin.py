from django.contrib import admin

from almacen.models import Almacen,Recepcion,Mercancia,Clasificaciones,Recepcionmercancias,Almacenmercancia,Vale,Valeitems
# Register your models here.
admin.site.register(Almacen)
admin.site.register(Recepcion)
admin.site.register(Mercancia)
admin.site.register(Clasificaciones)
admin.site.register(Recepcionmercancias)
admin.site.register(Almacenmercancia)
admin.site.register(Vale)