from django.conf.urls.defaults import *
import views
import models

urlpatterns = patterns('',
    (r'^$',             views.index),
    (r'^(?P<id>\d+)/$', views.update),
    (r'^new/$',         views.new),
    (r'^delete/$',      views.delete),
)
