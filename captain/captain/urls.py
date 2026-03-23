"""
URL configuration for captain project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from app1 import views as views1
from app2 import views  as views2
from app3 import views  as views3
urlpatterns = [
    path("admin/", admin.site.urls),
    
      path("app1/", views1.func1),
      path("app1/", views1.func2),
      path("app1/", views1.func3),
      path("app1/", views1.func4),
      
      path("app2/", views2.Operator1),
      path("app2/", views2.Operator2),
       path("app2/", views2.Operator3),
        path("app2/", views2.Operator4),
         path("app2/", views2.Operator5),
         
         path('app3/',views3.Algorithm1),
          path('app3/',views3.Algorithm2),
           path('app3/',views3.Algorithm3),
            path('app3/',views3.Algorithm4),
            path('app3/',views3.Algorithm5)
            
         
         
      
]
