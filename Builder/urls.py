from django.conf.urls import patterns, include, url
from Builder import views

urlpatterns = patterns('',   
    (r'^$', 'Builder.views.home_page'),
    (r'^accounts/login/$', 'Builder.views.user_login'),
)
