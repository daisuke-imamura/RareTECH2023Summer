from django.urls import path
from . import views


app_name = "antoquinoapp"

urlpatterns = [
    # path("regist/", views.regist, name="regist"),
    path("", views.hello, name="hello"),
    
]