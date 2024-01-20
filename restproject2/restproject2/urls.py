"""
URL configuration for restproject2 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from apiapp2 import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api1/',views.student_data.as_view()),
    path('api2/<int:id>/',views.student_data2.as_view()),
    path('api4/',views.student_data4.as_view()),
    path('api5/',views.StudentData5.as_view()),
    path('api6/',views.StudentData6.as_view())
]
