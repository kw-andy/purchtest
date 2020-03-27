"""trig_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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

# need to import views before creating the URL

#from django.conf.urls import patterns, include, url 
# #old use now : from django.conf.urls import *

from django.conf.urls import *
from django.contrib import admin
from django.urls import path,include
#from rest_framework import routers



from rest_framework.routers import DefaultRouter
from trig_app.views import *

router = DefaultRouter()
router.register(r'denomination', DenominationViewSet)
router.register(r'retailer', RetailerViewSet)



#urlpatterns = patterns('',
#    # Examples:
#    # url(r'^$', 'eboutique.views.home', name='home'),
#    # url(r'^blog/', include('blog.urls')),
#
#    url(r'^admin/', include(admin.site.urls)),
#    url(r'^api/', include(router.urls)),
#  #   url(r'^api/', include('rest_framework.urls', namespace='rest_framework'))
#)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('upload-file/',profile_upload,name='profile_upload'),
    path('home/',denom_list,name='denom_list'),
    path('api/',include(router.urls)),
]
