from django.contrib import messages
from .mixins import LoginRequiredMixin
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.urls import reverse
from django.views import View
from django.views.generic import TemplateView, FormView, CreateView, ListView, DetailView, UpdateView
from django.contrib.auth.views import LoginView as Login
from django.conf import settings
from .forms import EmailForm, RegistrationForm, ProfileForm
from django.contrib.auth import get_user_model, logout
from django.shortcuts import redirect
from django.http import HttpResponse
from .generate_token import account_activation_token
from .tasks import send_simple_email

User = get_user_model()


class EmailView(FormView):
    template_name = "users/send_email.html"
    form_class = EmailForm
    success_url = "/"

    def form_valid(self, form):
        response = super().form_valid(form)
        email = form.cleaned_data['email']
        subject = form.cleaned_data['subject']
        body = form.cleaned_data['body']
        send_simple_email.apply_async(kwargs={"body": body, "subject": subject,
                                              "email": email})
        return response


class RegistrationView(CreateView):
    form_class = RegistrationForm
    model = User
    success_url = '/'

    def form_valid(self, form):
        response = super().form_valid(form)
        subject = "Authenticate your Profile"
        user = self.object
        user.is_active = False
        user.save()
        token = account_activation_token.make_token(user)
        message = render_to_string("users/authentication.html",
                                   {"users": user,
                                    "domain": get_current_site(self.request),
                                    "token": token})
        email = EmailMessage(subject=subject, body=message,
                             from_email=settings.EMAIL_HOST_USER,
                             to=[user.email])
        email.send(fail_silently=False)
        messages.success(self.request, "User Created Successfully")
        return response


class ValidateUserLink(TemplateView):

    def get(self, request, *args, **kwargs):
        token = kwargs.get("token")
        pk = kwargs.get("pk")
        user = User.objects.get(pk=pk)
        if account_activation_token.check_token(user, token):
            user.is_active = True
            user.save()
            return redirect("users:login")
        return HttpResponse("Your token is invalid")


class LoginView(Login):
    pass


class LogoutView(View):
    def get(self, request, *args, **kwargs):
        # Perform logout logic
        logout(request)

        # Redirect to the home page after logout
        return redirect(reverse('home:home'))


class PasswordChangeDoneView(TemplateView):

    def get(self, request, **kwargs):
        messages.success(request, "Password changed successfully!")
        return redirect("users:user_profile")


class UserProfile(LoginRequiredMixin, DetailView):
    model = User
    template_name = "users/user_profile.html"


class UserUpdate(LoginRequiredMixin, UpdateView):
    model = User
    form_class = ProfileForm

    def get_success_url(self):
        messages.info(self.request, "User updated successfully!")
        return reverse("users:user_profile", kwargs={"pk": self.object.pk})

    def form_valid(self, form):
        result = super().form_valid(form)
        self.object.profile.country = form.cleaned_data["country"]
        self.object.profile.phone_number = form.cleaned_data["phone_number"]
        self.object.profile.image = form.cleaned_data["image"]
        self.object.profile.save()
        return result
