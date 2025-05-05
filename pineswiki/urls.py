# ----------------- urls.py
"""
URL configuration for django-wiki project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
import os,logging
from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

from django.conf import settings
from django.conf.urls.static import static
from wiki.urls import get_pattern as get_wiki_pattern
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

logger = logging.getLogger(__name__)

'''
Serving files uploaded by a user during development
https://docs.djangoproject.com/en/5.2/howto/static-files/#serving-files-uploaded-by-a-user-during-development
'''

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('', include('test_app.urls')),
    path('notifications/', include('django_nyt.urls')), #added for django-wiki
    #path('', lambda request: HttpResponse('Test custom HTTP response')),
    path('', include('wiki.urls')), #added for django-wiki 
    #path('', get_wiki_pattern()), #added for django-wiki 
] 
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
else:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()


#logger.warning(f'get_wiki_pattern()={get_wiki_pattern()}')
