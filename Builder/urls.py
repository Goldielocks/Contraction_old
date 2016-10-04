from django.conf.urls import include, url
from Builder.views import home_page, build, collaborate, publish, user_login

urlpatterns = [   
    url(r'^$', home_page),
    url(r'^Build/$', build),
    url(r'^Collaborate/$', collaborate),
    url(r'^Publish/$', publish),
    url(r'^accounts/login/$', user_login),
]
