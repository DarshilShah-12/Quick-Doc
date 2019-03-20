"""McHacks URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views
from django.views.generic import TemplateView
from .models import Search
from .models import add_search_form_submission

app_name = "main"

urlpatterns = [
    # path('', views.userForm, name="userForm"),
    path('', views.mainView.as_view(template_name='main/userForm.html')),
    path('dashboard.html', views.dashboardView.as_view(template_name='main/dashboard.html'))
    # path('add_search_form_submission/$', )
]
