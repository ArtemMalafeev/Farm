"""farm URL Configuration

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
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from ajax_select import urls as ajax_select_urls

from search import views as search_views

urlpatterns = [
    url(r'^ajax_select/', include(ajax_select_urls)),
    path('admin/', admin.site.urls),
    # path('search/', search_views.search_fertilizer),
    path('handbook/', include('handbook.urls', namespace='handbook')),
    # path('handbook/', include('handbook.urls', namespace='handbook')),
    path('fields/', include('fields.urls', namespace='fields')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
