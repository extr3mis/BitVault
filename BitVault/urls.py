"""BitVault URL Configuration

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
from django.urls import path, include
from django.contrib.auth.views import *
from django.conf import settings
from django.conf.urls.static import static

import home.views
from two_factor.urls import urlpatterns as tf_urls
from passwords.urls import urlpatterns as passwords_urls

urlpatterns = [
    path('', home.views.landingView, name='landing'),
    path('', include(tf_urls)),
    path('home/', include(passwords_urls)),
    path('account/change_password/', PasswordChangeView.as_view(), name="password_change"),
    path('account/change_password/done/', PasswordChangeDoneView.as_view(), name="password_change_done"),
    path('account/forgot_password/', PasswordResetView.as_view(), name="password_reset"),
    path('account/forgot_password/done/', PasswordResetDoneView.as_view(), name="password_reset_done"),
    path('account/reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path('account/reset/done/', PasswordResetCompleteView.as_view(), name="password_reset_complete"),
    path('signup/', home.views.SignUpView.as_view(), name="signup"),
    path('logout/', home.views.logoutView, name='logout'),
    path('admin/', admin.site.urls),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
