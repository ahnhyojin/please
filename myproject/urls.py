"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
import myapp.views
#media쓸때 습관처럼 써주기
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', myapp.views.index, name = 'index'),
    path('detail/<int:post_id>', myapp.views.detail, name = 'detail'),
    path('new/', myapp.views.new, name ='new'),
    path('create/', myapp.views.create, name = 'create'),
    path('edit/<int:post_id>', myapp.views.edit, name = 'edit'),
    path('editSend/<int:postupdate_id>',myapp.views.editSend, name = 'editSend'),
    path('askfor/', myapp.views.askfor, name = 'askfor'),
    
    path('accounts/', include('accountsapp.urls')),  # 최종 주소=> accounts/login or accounts/signup
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)   #r그냥 외우기
