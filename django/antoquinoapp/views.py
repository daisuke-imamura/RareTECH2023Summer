from django.shortcuts import render, redirect
from . import forms
from django.core.exceptions import ValidationError
import logging
from django.conf import settings




def hello(request):
    return render(
        request, "hello.html"
    )



# def regist(request):
#     regist_form = forms.RegistForm(request.POST or None)
#     if regist_form.is_valid():
#         try:
#             regist_form.save()
#             return redirect("antoquinoapp:recipe_list")
#         except ValidationError as e:
#             regist_form.add_error('password', e)
#     return render(
#         request, "regist.html", context={
#             "regist_form":regist_form,
#         }
#     )