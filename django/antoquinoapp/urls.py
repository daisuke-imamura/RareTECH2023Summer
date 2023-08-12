from django.urls import path
from . import views
from .forms import Loginform  
from .views import LoginView, LogoutView




app_name = "antoquinoapp"

urlpatterns = [
    path("", views.hello, name="hello"),
    path("regist/", views.regist, name="regist"),
    path('login/', LoginView.as_view(form_class=Loginform), name='login'),
    path('login/', LogoutView.as_view(), name='logout'),
    # path("recipe_list/", views.regist, name="recipe_list"),
    
]