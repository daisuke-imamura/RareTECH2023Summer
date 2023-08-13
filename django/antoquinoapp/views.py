from django.shortcuts import render, redirect
from . import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
from .models import Recipe
from .forms import RecipeCreateForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView



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
    

# class LogoutView(LogoutView):
#     template_name = 'login.html'


class RecipeCreateView(LoginRequiredMixin, CreateView):
    model = Recipe
    form_class = RecipeCreateForm
    template_name = 'recipe_create.html'
    
    def get_success_url(self):
        # return reverse_lazy('antoquinoapp:hello', kwargs={'pk': self.object.pk})
        return reverse_lazy('antoquinoapp:recipe_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class RecipeListView(ListView):
    model = Recipe
    form_class = RecipeCreateForm
    template_name = "recipe_list.html"
    
class RecipeDetailView(DetailView):
    model = Recipe
    form_class = RecipeCreateForm
    template_name = "recipe_detail.html"
    
class RecipeUpdateView(UpdateView):
    model = Recipe
    form_class = RecipeCreateForm
    template_name = "recipe_update.html"

    def form_valid(self, form):
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('antoquinoapp:recipe_detail', kwargs={'pk': self.object.pk})
    
class RecipeDeleteView(DeleteView):
    model = Recipe
    template_name = 'recipe_delete.html'
    success_url = reverse_lazy('antoquinoapp:recipe_list')



    
    