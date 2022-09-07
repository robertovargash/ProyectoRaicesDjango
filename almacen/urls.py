from unicodedata import name
from django.urls import path
from polls import views
from almacen.views import *

urlpatterns = [
    path('', views.home, name='home'),
    
    path('almacenes/', AlmacenesListView.as_view(), name='almacenes'),
    path('almacenes/nuevo', AlmacenesCreateView.as_view(), name='crear_almacen'),
    path('almacenes/<int:pk>/delete/', AlmacenesDeleteView.as_view(), name='eliminar_almacen'),
    path('almacenes/<int:pk>/update/', AlmacenesUpdateView.as_view(), name='editar_almacen'),

    path('clasificaciones/', ClasificacionesListView.as_view(), name='clasificaciones'),
    path('clasificaciones/nuevo', ClasificacionesCreateView.as_view(), name='crear_clasificacion'),
    path('clasificaciones/<int:pk>/delete/', ClasificacionesDeleteView.as_view(), name='eliminar_clasificacion'),
    path('clasificaciones/<int:pk>/update/', ClasificacionesUpdateView.as_view(), name='editar_clasificacion'),
        
    path('mercancias/', MercanciasListView.as_view(), name='mercancias'),
    path('mercancias/nuevo/', MercanciasCreateView.as_view(), name='crear_mercancias'),
    path('mercancias/<int:pk>/delete/', MercanciasDeleteView.as_view(), name='eliminar_mercancias'),
    path('mercancias/<int:pk>/update/', MercanciasUpdateView.as_view(), name='editar_mercancias'),
]