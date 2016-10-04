from django.conf.urls import include, url
from django.contrib import admin
from Builder.views import user_login

urlpatterns = [   
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('Builder.urls')),
    url(r'^accounts/login/$', user_login),
]
