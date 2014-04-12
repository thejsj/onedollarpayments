from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'onedollarpayments.views.home', name='home'),
    url(r'^pay-request/(?P<payment_request_hash>[-\w]+)/$', 'onedollarpayments.views.recepient_pay_request', name='recepient_pay_request'),
    url(r'^admin/', include(admin.site.urls)),
)
