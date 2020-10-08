"""PurBeurre_project URL Configuration

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
from django.conf import settings
from django.contrib import admin
from django.urls import include, path, re_path
from database_handler_app import views as database_handler_views
from user_app import views as user_views
from django.views.generic import TemplateView


urlpatterns = [
    re_path(r'^$', database_handler_views.index),
    re_path(r'^user_form/', user_views.user_form),
    # re_path(r'^user_myaccount/', user_views.user_myaccount),
    path('user_app/', include('user_app.urls')),
    path('database_handler_app/', include('database_handler_app.urls')),
    path('admin/', admin.site.urls),
    # path('accounts/profile/', user_views.user_myaccount, name='user_myaccount'),
    path('accounts/', include('django.contrib.auth.urls')),
    # path('accounts/profile/', ProfileViewsList.as_view()),
    path('accounts/profile/', TemplateView.as_view(template_name='user_app/profile.html'),
         name='profile'),
    # path('accounts/profile/', user_views.view_profile, name='view_profile'),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        re_path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns