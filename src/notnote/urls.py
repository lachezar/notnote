from django.conf.urls.defaults import *
from django.contrib import admin
from django.http import HttpResponseRedirect
import note.urls

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^notnote/', include('notnote.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    (r'^accounts/', include('socialauth.urls')),
    (r'^note/', include(note.urls)),
    (r'^note/$', 'socialauth.views.signin_complete'),
    (r'^accounts/logout$', 'socialauth.views.social_logout'),
    (r'^$', lambda x: HttpResponseRedirect('/note/')),
)

from django.conf import settings
if settings.DEBUG:
    urlpatterns += patterns('',
        # This is for the CSS and static files:
        (r'^media/(?P<path>.*)$', 'django.views.static.serve',
         {'document_root': settings.MEDIA_ROOT}),
    )
