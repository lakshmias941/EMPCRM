"""
URL configuration for employeecrm project.

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
from crm import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("employee/add",views.EmployeeCreateView.as_view(),name="emp-add"),
    path("employee/all",views.EmployeeListView.as_view(),name="emp-all"),
    path("employee/<int:pk>",views.EmployeeDetailView.as_view(),name="emp-detail"),
    path("employee/<int:pk>/remove",views.EmployeeDeleteView.as_view(),name="emp-delete"),
    path("employee/<int:pk>/change",views.EmployeeUpdateView.as_view(),name="emp-edit"),
    path("signup",views.SignUpView.as_view(),name="register"),
    path("",views.SignInview.as_view(),name="signin"),
    path("logout",views.SignOutView.as_view(),name="signout")
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
