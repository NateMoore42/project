from django.conf.urls import url
from django.views.generic import RedirectView
from . import views
from api.views import *
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^$', RedirectView.as_view(url="http://localhost:8000/api/endpoints/profile-list", permanent=True)),
    url(r'^user-list/$', views.UserList.as_view()),
    url(r'^profile-list/$', views.ProfileList.as_view(), name="profile-list"),
    url(r'^character-list/$', views.CharacterList.as_view()),
    url(r'^user-detail/(?P<pk>\w+)/$', views.UserDetail.as_view()),
    url(r'^profile-detail/(?P<pk>\w+)/$', views.ProfileDetail.as_view()),
    url(r'^character-detail/(?P<pk>\w+)/$', views.CharacterDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
