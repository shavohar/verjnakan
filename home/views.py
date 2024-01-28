from django.views.generic import ListView, TemplateView
from django.shortcuts import render
from home.models import AboutUs, WhyChooseUs, Chef,ContactUs


class Homepage(ListView):
    template_name = "home/home.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


class AboutUsView(TemplateView):
    template_name = 'home/about.html'

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


class ContactUsView(TemplateView):
    template_name = 'home/contact_us.html'

    def get(self, request, *args, **kwargs):
        contact_info = ContactUs.objects.all()

        context = {
            'contact_info': contact_info,
        }

        return render(request, self.template_name, context)