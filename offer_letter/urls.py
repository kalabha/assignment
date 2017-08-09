from django.conf.urls import include, url

from . import views

app_name = "offer_letter"


urlpatterns = [
        url(r'^create/$', views.create, name="create"),
        url(r'^(?P<pk>[^/]+)/', views.detail, name='detail'),
        

    ]
