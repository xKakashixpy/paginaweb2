from django import forms
from .models import Producto


class ProductFOrm(forms.ModelsForm):
    class Meta:
        model:Producto
        fields='__all__'