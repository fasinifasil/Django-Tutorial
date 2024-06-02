"""
URL configuration for userProject project.

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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from userApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.LoadHomepage, name='home'),
    path('gallery', views.LoadGallerypage, name='gallery'),
    path('student', views.register_student, name='register-student'),
    path('login', views.login_view, name='login'),

    path('staff', views.register_staff, name='register-staff'),
    path('admin', views.register_admin, name='register-admin'),
    path('editor', views.register_editor, name='register-editor'),
    path('adminregister', views.register_admin, name='register-admin'),
    path('editor', views.register_editor, name='register-editor'),
    path('admin-dashboard', views.AdminDashboard, name='admin-dashboard'),
    path('student-dashboard', views.StudentDashboard, name='student-dashboard'),
    path('staff-dashboard', views.StaffDashboard, name='staff-dashboard'),
    path('editor-dashboard', views.EditorDashboard, name='editor-dashboard'),
    path('logout', views.logout, name='logout'),

]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)