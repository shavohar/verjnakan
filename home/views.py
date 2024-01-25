from django.views.generic import ListView
from django.shortcuts import render


class Homepage(ListView):
    template_name = "home/home.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
