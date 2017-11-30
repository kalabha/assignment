"""assignment URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include, url
from address import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^$', views.userlogin, name="signin"),
    # url(r'^login/$', views.userlogin, name="login"),
    # url(r'^logout/$', views.userlogout, name="logout"),
    # url(r'^offer_letter/', include('offer_letter.urls', namespace="offer_letter")),
    url(r'^get_address/(?P<get_latitude>[^/]+)/(?P<get_longitude>[^/]+)/$', views.get_address, name="get_address"),

]
