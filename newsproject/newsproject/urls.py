"""newsproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path,include
from newsapp import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_page_view),
    path('world/', views.world_view),
    path('science/', views.science_view),
    path('sports/', views.sports_view),
    path('technology/', views.technology_view),
    path('health/', views.health_view),
    path('entertainment/', views.entertainment_view),
    path('logout/', views.logout_view),
    path('signup/', views.signup_view),
    path('general/', views.general_view),
    path('news/', views.news_view),
    path('india/', views.india_view),
    path('us/', views.us_view),
    path('ca/', views.ca_view),
    path('au/', views.australia_view),
    path('gb/', views.gb_view),
    path('my/', views.my_view),
    path('za/', views.za_view),
    path('sg/', views.sg_view),
    path('nz/', views.nz_view),
    path('search/', views.search_view,name="search"),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name="registration/password_reset.html"), name="password_reset"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="registration/password_reset_sent.html"), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="registration/password_reset_form.html"), name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="registration/password_reset_done.html"), name="password_reset_complete"),
    path('accounts/',include('django.contrib.auth.urls')),
]
