from django import forms
from .models import Item


class PizzaForm(forms.ModelForm):

    class Meta:
        model = Item
        fields = ("name", "description",
                  "prepare_time", "calories",
                  "price", "image", "category")
