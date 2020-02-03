"""EmpMangSys URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib.auth.decorators import login_required
from django.urls import path
from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('', views.StaffLogin.as_view(), name="StaffLogin"),  # First page and for login page for staff
    path('contact/', views.contact_us, name="contact_us"),
    path('home/', views.home_page, name="home_page"),
    path('',views.StaffLogin.as_view(),name="StaffLogin"),
    path('EmpReg/', views.EmpReg,name="EmpReg"),                           #first page and register form
    path('SaveEmpData/', views.SaveEmpData.as_view(),name="SaveEmpData"),   #for saving data into database
    path('empData/',views.DisplayEmpData.as_view(),name="empData"),
    path('showStudData/',views.showStudData,name="showStudData"),
    ##Display information of employee from DB
    path('studReg/', views.studReg,name="studReg"),                           #first page and register form
    path('saveStudData/', views.saveStudData.as_view(),name="saveStudData"),   #for saving data into database
    path('studData/',views.DisplayStudData.as_view(),name="studData"),
    path('logout/',views.logout1,name="logout"),

    # path('SaveEmpData/', views.SaveEmpData.as_view(), name="SaveEmpData"),  # for saving data into database
    # path('empData/', views.DisplayEmpData.as_view(), name="empData"),  ##Display information of employee from DB
    # path('logout/', views.logout1, name="logout"),  # logout user

    # path('success/',views.success,name="success"),
]
