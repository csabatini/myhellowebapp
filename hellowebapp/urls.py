from collection.backends import MyRegistrationView
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView, RedirectView
from django.contrib.auth.views import (
    password_reset,
    password_reset_done,
    password_reset_confirm,
    password_reset_complete
)
urlpatterns = patterns('',
    url(r'^$', 'collection.views.index', name='home'),
    url(r'^about/$', TemplateView.as_view(template_name='about.html'), name='about'),
    url(r'^contact/$', TemplateView.as_view(template_name='contact.html'), name='contact'),

    # collection urls
    url(r'^stocks/(?P<slug>[-\w]+)/$', 'collection.views.stock_detail', name='stock_detail'),
    url(r'^stocks/(?P<slug>[-\w]+)/edit/$', 'collection.views.edit_stock', name='edit_stock'),
    url(r'^browse/symbol/$', 'collection.views.browse_by_symbol', name='browse'),
    url(r'^browse/symbol/(?P<initial>[-\w]+)/$', 'collection.views.browse_by_symbol', name='browse_by_symbol'),
    # TODO: automated test for redirects
    url(r'^browse/$', RedirectView.as_view(pattern_name='browse', permanent=False)),
    url(r'^stocks/$', RedirectView.as_view(pattern_name='browse', permanent=False)),

    # password reset urls
    url(r'^accounts/password/reset/$', password_reset,
        {'template_name':'registration/password_reset_form.html'}, name='password_reset'),
    url(r'^accounts/password/reset/done/$', password_reset_done,
        {'template_name':'registration/password_reset_done.html'}, name='password_reset_done'),
    url(r'^accounts/password/reset/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', password_reset_confirm,
        {'template_name': 'registration/password_reset_confirm.html'}, name='password_reset_confirm'),
    url(r'^accounts/password/done/$', password_reset_complete,
        {'template_name': 'registration/password_reset_complete.html'}, name='password_reset_complete'),

    # registration urls
    url(r'^accounts/register/$', MyRegistrationView.as_view(), name='registration_register'),
    url(r'^accounts/add_stock/$', 'collection.views.add_stock', name='registration_add_stock'),
    url(r'^accounts/', include('registration.backends.simple.urls')),

    url(r'^admin/', include(admin.site.urls)),
)

