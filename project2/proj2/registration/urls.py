from . import views
from django.urls import path

urlpatterns = [

    path('signin', views.signin, name='signin'),
    # path('login', views.login, name='login'),
    path('log', views.log, name='log'),
    path('logout', views.logout, name='logout')
]