from django.urls import path, include
# from user_app.views import ProfileViewsList
from . import views

urlpatterns = [
    path('', views.user_form, name='user_form'),
    # path('', views.user_myaccount, name='user_myaccount'),
    # path('accounts/', include('django.contrib.auth.urls')),
    # path('accounts/profile/', ProfileViewsList.as_view()),
]
