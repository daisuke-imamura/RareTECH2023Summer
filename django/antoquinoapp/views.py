from django.shortcuts import render, redirect
from . import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView







def hello(request):
    return render(
        request, "hello.html"
    )


def regist(request):
    regist_form = forms.RegistForm(request.POST or None)
    if regist_form.is_valid():
        try:
            regist_form.save()
            return redirect("antoquinoapp:login")
            # return redirect("antoquinoapp:hello")
        except ValidationError as e:
            regist_form.add_error('password', e)
    return render(
        request, "regist.html", context={
            "regist_form":regist_form,
        }
    )
    
class LoginView(LoginView):
    template_name = "login.html"
    form_class = forms.Loginform
    

class CustomLogoutView(LogoutView):
    template_name = 'login.html'

class RecipeCreateView(CreateView):
    