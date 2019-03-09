from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^animals/$', views.animals, name='animals'),
    url(r'^animals/(?P<animal_id>\d+)/$', views.animal, name='animal'),
    url(r'^animals/(?P<animal_id>\d+)/edit/$', views.animal_edit, name='animal_edit'),
    url(r'^animals/(?P<animal_id>\d+)/delete/$', views.delete_animal, name='delete_animal'),
    url(r'^animals/(?P<animal_id>\d+)/delete-confirm/$', views.delete, name='delete'),
    url(r'^animals/add/$', views.create_animal, name='create_animal'),
    url(r'^search/$', views.search, name='search'),
    url(r'^login/$', views.login_user, name='login_user'),
    url(r'^logout/$', views.logout_user, name='logout_user'),
    url(r'^contacts/$', views.Contact.as_view(), name='contacts'),
    url(r'^questions/$', views.Questions.as_view(), name='questions'),

]