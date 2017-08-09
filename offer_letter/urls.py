from django.conf.urls import include, url

from . import views

app_name = "offer_letter"


urlpatterns = [
    	url(r'^$', views.index, name="index"),
        url(r"^(?P<pk>[^/]+)_offer_letter.pdf/$", views.OfferLetterPDFView.as_view(),name="letter"),
        url(r'^create/$', views.create, name="create"),
        url(r'^(?P<pk>[^/]+)/$', views.detail, name='detail'),

    ]
