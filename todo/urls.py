from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.get_all, name='index'),
    url(r'(?P<id>[0-9]+)', views.get_single, name='single'),
    url(r'^post/(?P<text>\w{1,150})', views.post, name="post"),
    url(r'^delete/$', views.delete, name='delete')
]