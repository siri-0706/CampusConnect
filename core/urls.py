from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('issue/new/', views.create_issue, name="create_issue"),
]
