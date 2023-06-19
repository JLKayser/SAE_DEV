from django.urls import path
from . import views

urlpatterns = [
    path('', views.LoginClient, name='login_client'),
    path('login/client', views.LoginClient, name='login_client'),
    path('login/personnel', views.LoginPersonnel, name='login_personnel'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('depot', views.depot, name='depot'),
    path('prelevement', views.prelevement, name='prelevement'),
    path('virement', views.virement, name='virement'),
    path('creation_compte', views.creation_compte, name='creation_compte'),
    path('creation_client', views.SignupClient, name='creation_client'),
    path('creation_personnel', views.SignupPersonnel, name='creation_personnel'),
    path('logout', views.logoutUser, name='lougoutClient'),
]
