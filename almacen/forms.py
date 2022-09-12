from cProfile import label
from distutils.text_file import TextFile
from pyexpat import model
from turtle import textinput
from django.forms import *
from almacen.models import Almacen,Clasificaciones, Mercancia, Recepcion

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
    codigo = CharField(label='Code',widget=TextInput(attrs={'class':'form-control','placeholder':'Código'}))
    nombremercancia = CharField(label='Nombre',widget=TextInput(attrs={'class':'form-control', 'placeholder':'Nombre'}))
    um = CharField(label='UM',widget=TextInput(attrs={'class':'form-control', 'placeholder':'UM'}))
    clasificacion = ClasificacionesModelChoiceField(
                                            label='Clasificación',
                                            queryset=Clasificaciones.objects.all(), empty_label='Seleccione: ', 
                                            widget=Select(attrs={'style':'width: 100%', 'class':'form-control select2bs4'}))
    descripcion = CharField(label='Descripción',widget=Textarea(attrs={'style':'height:150px', 'class':'form-control', 'placeholder':'Descripción'}))
    class Meta:
        model = Mercancia
        # fields='__all__'
        fields = ['codigo', 'nombremercancia','um','clasificacion','descripcion']
        # labels = {
        #     'codigo': 'Código',
        #     'nombremercancia': 'Nombre',
        #     'clasificacion':'Clasificación',
        #     'um': 'UM',
        #     'descripcion': 'Descripción'
        # }
        # widgets = {
        #     'codigo': TextInput( attrs={ 'class':'form-control', 'placeholder':'Código' }),
        #     'nombremercancia': TextInput(attrs={ 'class':'form-control', 'placeholder':'Nombre'}),
        #     'um': TextInput(attrs={ 'class':'form-control', 'placeholder':'UM' }),
        #     'clasificacion' : Select(attrs={'style':'width: 100%', 'class':'form-control select2bs4'}),
        #     'descripcion': Textarea( attrs={ 'style':'height:150px', 'class':'form-control', 'placeholder':'Descripción' } ),
        # }

class AddRecepcionForm(ModelForm):
    class Meta:
        model = Recepcion
        fields = ['proveedor', 'contrato','factura','precibe','pentrega','pautoriza','observaciones']
        exclude = ['almacen','numero']
        labels = {'proveedor': 'Proveedor','contrato': 'Contrato','factura':'Factura','precibe': 'Recibe','pentrega': 'Entrega','pautoriza': 'Autoriza','observaciones': 'Observaciones'}
        widgets = {
            'proveedor': TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Proveedor'
                }
            ),
            'contrato': TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Contrato'
                }
            ),
            'factura': TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Factura'
                }
            ),
            'precibe': TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Recibe'
                }
            ),
             'pentrega': TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Entrega'
                }
            ),
             'pautoriza': TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Autoriza'
                }
            ),
            'observaciones': Textarea(
                attrs={
                    'style':'height:150px',
                    'class':'form-control',
                    'placeholder':'Observaciones'
                }
            ),
        }

class EditRecepcionForm(ModelForm):
    class Meta:
        model = Recepcion
        fields = ['fecha','proveedor', 'contrato','factura','precibe','pentrega','pautoriza','observaciones']
        exclude = ['almacen','numero','activo']
        labels = {'fecha': 'Fecha','proveedor': 'Proveedor','contrato': 'Contrato','factura':'Factura','precibe': 'Recibe','pentrega': 'Entrega','pautoriza': 'Autoriza','observaciones': 'Observaciones'}
        widgets = {
            'fecha' : TextInput(
                attrs={
                    'readonly':'readonly',
                    'class':'form-control',
                }
            ),
            'proveedor': TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Proveedor'
                }
            ),
            'contrato': TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Contrato'
                }
            ),
            'factura': TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Factura'
                }
            ),
            'precibe': TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Recibe'
                }
            ),
             'pentrega': TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Entrega'
                }
            ),
             'pautoriza': TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Autoriza'
                }
            ),
            'observaciones': Textarea(
                attrs={
                    'style':'height:150px',
                    'class':'form-control',
                    'placeholder':'Observaciones'
                }
            ),
        }


class RecepcionForm(ModelForm):
    class Meta:
        model = Recepcion
        # fields='__all__'
        fields = ['proveedor', 'contrato','factura','precibe','pentrega','pautoriza','observaciones']
        labels = {            
            'proveedor': 'Proveedor',
            'contrato': 'Contrato',
            'factura':'Factura',
            'precibe': 'Recibe',
            'pentrega': 'Entrega',
            'pautoriza': 'Autoriza',
            'observaciones': 'Observaciones'
        }
        widgets = {   
            'proveedor': TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Proveedor'
                }
            ),
            'contrato': TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Contrato'
                }
            ),
            'factura': TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Factura'
                }
            ),
            'precibe': TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Recibe'
                }
            ),
             'pentrega': TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Entrega'
                }
            ),
             'pautoriza': TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Autoriza'
                }
            ),
            'observaciones': Textarea(
                attrs={
                    'style':'height:150px',
                    'class':'form-control',
                    'placeholder':'Observaciones'
                }
            ),
        }