from django.urls import path
from . import views
from .forms import Loginform  
from .views import LoginView, LogoutView, RecipeCreateView




app_name = "antoquinoapp"

urlpatterns = [
    path("", views.hello, name="hello"),
    path("regist/", views.regist, name="regist"),
    path('login/', views.LoginView.as_view(form_class=Loginform), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('recipe_create/', views.RecipeCreateView.as_view(), name='recipe_create'),
    path('recipe_list/', views.RecipeListView.as_view(), name='recipe_list'),
    path('recipe_detail/<int:pk>', views.RecipeDetailView.as_view(), name='recipe_detail'),
    path('recipe_update/<int:pk>', views.RecipeUpdateView.as_view(), name='recipe_update'),
    path('recipe_delete/<int:pk>', views.RecipeDeleteView.as_view(), name='recipe_delete'),
]
    # path("recipe_list/", views.regist, name="recipe_list"),
    