from django.conf.urls import patterns, include, url
from django.views.generic import DetailView, ListView
from quests.models import *

urlpatterns = patterns('quests.views',
    url(r'^$', 'index'),
    )

urlpatterns += patterns('quests.views',
    url(r'^user/(?P<user_id>\d+)/$', 'profile'),
    url(r'^open/$', 'quest'),
    url(r'^group/(?P<group_id>\d+)/$', 'group'),
    # url(r'', ''), 
    )
