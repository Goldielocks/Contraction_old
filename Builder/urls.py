from django.conf.urls import patterns, include, url
from Builder import views

urlpatterns = patterns('',   
    (r'^$', 'Builder.views.home_page'),
    (r'^Build/$', 'Builder.views.build'),
    (r'^Collaborate/$', 'Builder.views.collaborate'),
    (r'^Publish/$', 'Builder.views.publish'),
    (r'^accounts/login/$', 'Builder.views.user_login'),
)
