from django.conf.urls import patterns, include, url
from Builder import views

urlpatterns = patterns('',
	(r'^case/$', 'Builder.views.get_case'),
    (r'^case_save/$', 'Builder.views.save_case'),
    (r'^case_add/$', 'Builder.views.add_case'),
    (r'^move_case/$', 'Builder.views.move_case'),
    (r'^link_case/$', 'Builder.views.link_case'),   
    (r'^$', 'Builder.views.home_page'),
    (r'^accounts/login/$', 'Builder.views.user_login'),
)
