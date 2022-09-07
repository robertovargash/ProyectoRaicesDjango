from cProfile import label
from distutils.text_file import TextFile
from pyexpat import model
from turtle import textinput
from django.forms import *
from almacen.models import Almacen,Clasificaciones, Mercancia

class AlmacenesForm(ModelForm):
    class Meta:
        model = Almacen
        fields = ['almacen', 'descripcion']
        labels = {
            'almacen': 'Almacén',
            'descripcion': 'Descripción'
        }
        widgets = {
            'almacen': TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Almacén'
                }
            ),
            'descripcion': Textarea(
                attrs={
                    'style':'height:150px',
                    'class':'form-control',
                    'placeholder':'Descripción'
                }
            ),
        }

class ClasificacionesForm(ModelForm):
    class Meta:
        model = Clasificaciones
        # fields = '__all__'
        fields = ['clasificacion', 'detalles']
        labels = {
            'clasificacion': 'Clasificación',
            'detalles': 'Detalles'
        }
        widgets = {
            'clasificacion': TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Clasificación'
                }
            ),
            'detalles': Textarea(
                attrs={
                    'style':'height:150px',
                    'class':'form-control',
                    'placeholder':'Detalles'
                }
            ),
        }

# devuelve el campo que desee del select, en vez del ID, en este caso, el atributo clasificacion
class ClasificacionesModelChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return (obj.clasificacion)

class MercanciasForm(ModelForm):
    # codigo = CharField(label='Code',widget=TextInput(attrs={'class':'form-control','placeholder':'Código'}))
    # nombremercancia = CharField(label='Nombre',widget=TextInput(attrs={'class':'form-control', 'placeholder':'Nombre'}))
    # um = CharField(label='UM',widget=TextInput(attrs={'class':'form-control', 'placeholder':'UM'}))
    # clasificacion = ClasificacionesModelChoiceField(label='Clasificación',queryset=Clasificaciones.objects.all(), empty_label='Seleccione: ', widget=Select(attrs={'style':'width: 100%', 'class':'form-control select2bs4'}), to_field_name='clasificacion')
    # descripcion = CharField(label='Descripción',widget=Textarea(attrs={'style':'height:150px', 'class':'form-control', 'placeholder':'Descripción'}))
    class Meta:
        model = Mercancia
        # fields='__all__'
        fields = ['codigo', 'nombremercancia','um','clasificacion','descripcion']
        labels = {
            'codigo': 'Código',
            'nombremercancia': 'Nombre',
            'clasificacion':'Clasificación',
            'um': 'UM',
            'descripcion': 'Descripción'
        }
        widgets = {
            'codigo': TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Código'
                }
            ),
            'nombremercancia': TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Nombre'
                }
            ),
            'um': TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'UM'
                }
            ),
            'clasificacion' : Select(attrs={'style':'width: 100%', 'class':'form-control select2bs4'}),
            'descripcion': Textarea(
                attrs={
                    'style':'height:150px',
                    'class':'form-control',
                    'placeholder':'Descripción'
                }
            ),
        }