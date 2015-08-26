
from django.conf.urls import include, url,patterns
from django.contrib import admin
from blog import views
admin.autodiscover()


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$',views.post_list,name='index'),
    url(r'^post/(?P<pk>[0-9]+)/$',views.post_detail,name='detail'),
    url(r'^post/new/$',views.post_new,name='new'),
    url(r'^post/(?P<pk>[0-9]+)/edit/$',views.post_edit,name='edit'),
    url(r'^drafts/$',views.post_draft_list,name='postdraftlist'),
    url(r'^post/(?P<pk>[0-9]+)/publish/$',views.post_publish,name='post_publish'),
    url(r'^post/(?P<pk>[0-9]+)/remove/$',views.post_remove,name='post_remove'),
    url(r'^accout/login/$','django.contrib.auth.views.login'),
    url(r'^accout/logout/$','django.contrib.auth.views.logout',{'next_page':'/'}),
    url(r'^about/',views.about),
    url(r'^comment/add/(?P<pk>[0-9]+)/$',views.add_comment,name='add_comment'),


]
