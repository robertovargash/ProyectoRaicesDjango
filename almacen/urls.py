from unicodedata import name
from django.urls import path
from django.contrib.auth import views as auth_views
from almacen.views import *

urlpatterns = [
    # path('', views.home, name='home'),
    
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


    path('recepcion/nuevo/', RecepcionCreateView.as_view(), name='crear_recepcion'),
    # path('recepcion/nuevo/', add_recepcion_view, name='crear_recepcion'),
    # path('recepcion/<int:pk>/update/', edit_recepcion_view, name='editar_recepcion'),
    # path('editarecepcion', edit_recepcion,name='editar_recepcionpost'),
    # path('recepcion/<int:pk>/delete/', delete_recepcion_view, name='eliminar_recepcion'),
    # path('recepcion/<int:pk>/delete/', RecepcionDeleteView.as_view(), name='eliminar_recepcion'),
    path('recepcion/<int:pk>/update/', RecepcionUpdateView.as_view(), name='editar_recepcion'),
    path('recepcion/<int:pk>/cancelar/', cancelar_recepcion,name='cancelar_recepcion'),
    path('recepcion/<int:pk>/firmar/', firmar_recepcion,name='firmar_recepcion'),

    path('recepcionmercancia/nuevo/', RecepcionmercanciaCreateView.as_view(), name='crear_recepcion_mercancia'),
    path('recepcionmercancia/<int:pk>/delete/', RecepcionmercanciaDeleteView.as_view(), name='eliminar_recepcionmercancia'),
    path('recepcionmercancia/<int:pk>/update/', RecepcionmercanciaUpdateView.as_view(), name='editar_recepcionmercancia'),
]