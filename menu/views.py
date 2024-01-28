from django.views.generic import ListView
from .models import Item


class ItemsListView(ListView):
    template_name = "menu/menu.html"
    context_object_name = "items"
    paginate_by = 2
    queryset = Item.objects.all().order_by("-pk")
