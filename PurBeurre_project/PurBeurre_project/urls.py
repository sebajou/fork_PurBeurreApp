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
from django.contrib.auth.views import LoginView


urlpatterns = [
    re_path(r'^$', database_handler_views.index, name='index'),
    re_path(r'^user_form/', user_views.user_form, name='user_form'),
    re_path(r'^search_results/', database_handler_views.search_results, name='search_results'),
    re_path(r'^legal_mention/', database_handler_views.legal_mention, name='legal_mention'),
    re_path(r'^my_foods/', database_handler_views.my_foods, name='my_foods'),
    # re_path(r'^accounts/login/$', user_views.profile, name='profile'),
    # re_path(r'^accounts/login/$', LoginView.as_view(redirect_authenticated_user=True)),

    path('database_handler_app/search_results/', database_handler_views.search_results, name='search_results'),
    path('database_handler_app/legal_mention/', database_handler_views.legal_mention, name='legal_mention'),
    path('database_handler_app/my_foods/', database_handler_views.my_foods, name='my_foods'),
    path('admin/', admin.site.urls),
    path('database_handler_app/accounts/login/', TemplateView.as_view(template_name='registration/login.html'), name='login'),
    path('database_handler_app/accounts/logout/', TemplateView.as_view(template_name='registration/logged_out.html'), name='logout'),
    path('accounts/profile/', user_views.profile, name='profile'),

    path('user_app/', include('user_app.urls')),
    path('database_handler_app/', include('database_handler_app.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        re_path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns