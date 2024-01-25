from django.shortcuts import render
from django.views import View
from .models import AboutUs, WhyChooseUs, Chef


class AboutUsListView(View):
    template_name = 'about/about.html'

    def get(self, request, *args, **kwargs):
        about = AboutUs.objects.all()
        why_choose_us = WhyChooseUs.objects.all()
        chef = Chef.objects.all()

        context = {
            'about': about,
            'why_choose_us': why_choose_us,
            'chef': chef,
        }

        return render(request, self.template_name, context)
