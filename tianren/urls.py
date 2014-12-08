from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views

admin.autodiscover()

from tianren.views import hello, hours_ahead
#from tianren.datamodel.admin import initiation_admin_site, people_admin_site, donation_admin_site, temple_admin_site

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'tianren.views.home', name='home'),
    url(r'^home/plus/(\d{1,2})/$', hours_ahead),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include( admin.site.urls ) ),
    # url(r'^admin/initiation/', include( initiation_admin_site.urls ) ),
    # url(r'^admin/people/', include( people_admin_site.urls ) ),
    # url(r'^admin/temple/', include( temple_admin_site.urls ) ),
    # url(r'^admin/donation/', include( donation_admin_site.urls ) ),
    
    
    url(r'^hello/$', hello )
    
    # url(r'^admin/password_reset/$', auth_views.password_reset, name='admin_password_reset'),
    # url(r'^admin/password_reset/done/$', auth_views.password_reset_done, name='password_reset_done'),
    # url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$', auth_views.password_reset_confirm, name='password_reset_confirm'),
    # url(r'^reset/done/$', auth_views.password_reset_complete, name='password_reset_complete'),    
)
