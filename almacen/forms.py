from django.forms import *
from almacen.models import Almacen,Clasificaciones, Mercancia, Recepcion, Recepcionmercancias
from django.utils.translation import gettext_lazy as _

class AlmacenesForm(ModelForm):
    class Meta:
        model = Almacen
        fields = ['almacen', 'descripcion']
        labels = {
            'almacen': _('Store_Name'),
            'descripcion': _('Store_Details')
        }
        widgets = {
            'almacen': TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':_('Store_Name')
                }
            ),
            'descripcion': Textarea(
                attrs={
                    'style':'height:150px',
                    'class':'form-control',
                    'placeholder':_('Store_Details')
                }
            ),
        }

class ClasificacionesForm(ModelForm):
    class Meta:
        model = Clasificaciones
        # fields = '__all__'
        fields = ['clasificacion', 'detalles']
        labels = {
            'clasificacion': _('Clasification_Name'),
            'detalles':  _('Clasification_Details')
        }
        widgets = {
            'clasificacion': TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':_('Clasification_Name')
                }
            ),
            'detalles': Textarea(
                attrs={
                    'style':'height:150px',
                    'class':'form-control',
                    'placeholder':_('Clasification_Details')
                }
            ),
        }

# devuelve el campo que desee del select, en vez del ID, en este caso, el atributo clasificacion
class ClasificacionesModelChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return (obj.clasificacion)

class MercanciasForm(ModelForm):
    codigo = CharField(label=_('Product_Code'),widget=TextInput(attrs={'class':'form-control','placeholder':_('Product_Code')}))
    nombremercancia = CharField(label=_('Product_Name'),widget=TextInput(attrs={'class':'form-control', 'placeholder':_('Product_Name')}))
    um = CharField(label=_('Product_UM'),widget=TextInput(attrs={'class':'form-control', 'placeholder':_('Product_UM')}))
    clasificacion = ClasificacionesModelChoiceField(
                                            label=_('Product_Clasification'),
                                            queryset=Clasificaciones.objects.all(), empty_label=_('Product_SelectClasificationLabel'), 
                                            widget=Select(attrs={'style':'width: 100%', 'class':'form-control select2bs4'}))
    descripcion = CharField(label=_('Product_Details'),widget=Textarea(attrs={'style':'height:150px', 'class':'form-control', 'placeholder':_('Product_Details')}))
    class Meta:
        model = Mercancia
        # fields='__all__'
        fields = ['codigo', 'nombremercancia','um','clasificacion','descripcion']
    
    
class RecepcionForm(ModelForm):
    class Meta:
        model = Recepcion
        # fields='__all__'
        fields = ['proveedor', 'contrato','factura','pentrega','observaciones']
        labels = {            
            'proveedor': _('Reception_Provider'),
            'contrato': _('Reception_Contract'),
            'factura':_('Reception_Invoice'),
            'pentrega': _('Reception_P_Deliver'),
            'observaciones': _('Reception_Details')
        }
        widgets = {   
            'proveedor': TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':_('Reception_Provider')
                }
            ),
            'contrato': TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':_('Reception_Contract')
                }
            ),
            'factura': TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':_('Reception_Invoice')
                }
            ),
             'pentrega': TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':_('Reception_P_Deliver')
                }
            ),
            'observaciones': Textarea(
                attrs={
                    'style':'height:150px',
                    'class':'form-control',
                    'placeholder':_('Reception_Details')
                }
            ),
        }

class AddRecepcionmercanciaForm(ModelForm):    
    mercancia = ModelChoiceField(label=_('ReceptionProduct_Product'),queryset=Mercancia.objects.all(), empty_label=_('Reception_SelectProductLabel'), 
                                            widget=Select(attrs={'style':'width: 100%', 'class':'form-control select2bs4'}))
    cantidad = CharField(label=_('ReceptionProduct_Quantity'),widget=NumberInput(attrs={'class':'form-control','placeholder':_('ReceptionProduct_Quantity')}))
    precio = CharField(label=_('ReceptionProduct_Price'),widget=NumberInput(attrs={'class':'form-control', 'placeholder':_('ReceptionProduct_Price')}))
    class Meta:
        model = Recepcionmercancias
        # fields = '__all__'
        fields = ['mercancia','cantidad','precio']

class EditRecepcionmercanciaForm(ModelForm):    
    cantidad = DecimalField(label=_('ReceptionProduct_Quantity'),widget=NumberInput(attrs={'class':'form-control','placeholder':_('ReceptionProduct_Quantity'),'id':'cantidad_ele'}))
    precio = DecimalField(label=_('ReceptionProduct_Price'),widget=NumberInput(attrs={'class':'form-control', 'placeholder':_('ReceptionProduct_Price'),'id':'precio_ele'}))
    class Meta:
        model = Recepcionmercancias
        # fields = '__all__'
        fields = ['cantidad','precio']