"""
URL configuration for Nimap project.

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
from api1.views import ClientDetail,ClientwithprojectDetail,ClientCreate,ClientUpdate,ClientDelete,ProjectDetail,ProjectCreate
# from api1 import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('clientdetail/<int:id>/', ClientDetail.as_view(), name='client-detail'),
    path('clientsalldetail/<int:id>/', ClientwithprojectDetail.as_view(), name='client-detail'),
    path('clientscreate/', ClientCreate.as_view(), name='client-create'),
    path('clientsupdate/<int:id>/', ClientUpdate.as_view(), name='client-update'),
    path('clientsdelete/<int:pk>/', ClientDelete.as_view(), name='client-delete'),
    # path('projectcreate/<int:client_id>/projects/', ProjectCreate.as_view(), name='project-create'),
    path('projectdetail/<int:id>/', ProjectDetail.as_view(), name='client-detail'),
    # path('projects/', ProjectCreate.as_view(), name='project-create'),
    path('projects/create/', ProjectCreate.as_view(), name='project-create'),


]
