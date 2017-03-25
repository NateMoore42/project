from django.conf.urls import url
from . import views
from Auth.views import *

urlpatterns = [
    # Standard URLS
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^profile/(?P<username>\w+)/$', views.get_user_profile, name='profile'),
    url(r'^profile/edit/(?P<username>\w+)/$', views.user_profile_edit, name='profile_edit'),
]
