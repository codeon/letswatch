from django.conf.urls.defaults import patterns, include, url
from views import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
	'',
    # Examples:
    #~ url(r'^$', 'letswatch_django.views.home', name='home'),
    #~ url(r'^letswatch_django/', include('letswatch_django.foo.urls')),
	url(r'^home', home),
    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    
)

urlpatterns += staticfiles_urlpatterns()
