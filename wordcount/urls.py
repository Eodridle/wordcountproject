"""wordcount URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
#from django.contrib import admin
from django.urls import path
from . import views #. is this directory

urlpatterns = [
    path('', views.home),
    path('count/', views.count, name='count'), #This url is connected to the count.html through the third parameter. You can connect it through the first parameter
    path('about/', views.about, name='about'),
    #however the instructor says that its not good practice because the url could change and it would break the code.
    #path('eggs/', views.eggs), #Good practice to put a slash at the end of the path
    #path('admin/', admin.site.urls),
]
