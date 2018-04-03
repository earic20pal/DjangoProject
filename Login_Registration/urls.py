from django.conf.urls import url
from django.contrib import admin

from Login_Registration import views
urlpatterns = [
url(r'^admin/', admin.site.urls),
url(r'^$', views.SiddhuList.as_view(), name='siddhu_list'),
url(r'^insert$', views.SiddhuInsert.as_view(), name='siddhu_insert'),
url(r'^update/(?P<pk>\d+)$', views.SiddhuUpdate.as_view(), name='siddhu_update'),
url(r'^delete/(?P<pk>\d+)$', views.SiddhuDelete.as_view(), name='siddhu_delete'),
]
