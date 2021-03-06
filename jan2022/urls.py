"""jan2022 URL Configuration

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
from django.contrib import admin
from django.urls import path
from registrationapp import views as regist_views
from homeapp import views as home_views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from homeapp.views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', regist_views.register, name='register'),
    path('profile/', home_views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='registrationapp/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='registrationapp/logout.html'), name='logout'),
    path('home/', PostListView.as_view(), name='home'),
    path('post-detail/<int:pk>', PostDetailView.as_view(), name='post-detail'),
    path('newpost/', PostCreateView.as_view(), name='post-create'),
    path('post-detail/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post-detail/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete')
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
