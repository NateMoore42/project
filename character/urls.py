from django.conf.urls import url
from . import views
from character.views import *

urlpatterns = [
    # Standard URLS
    url(r'^create/', views.character_create, name='create_character'),
    url(r'^character/(?P<pk>\w+)/$', views.character_detail, name='character_detail'),
    url(r'^character/edit/(?P<pk>\w+)/(?P<c_name>\w+)/$', views.character_edit, name='character_edit'),
]
