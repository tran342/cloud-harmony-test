from django.conf.urls import url
from django.contrib import admin

from cgroup_management.views import CGroupPidView, CGroupView

urlpatterns = [
    url(r'^cgroup/(?P<name>\w+)$', CGroupView.as_view(), name='cgroup-modify'),
    url(r'^cgroup/(?P<name>\w+)/pid$', CGroupPidView.as_view(), {'pid': None}, name='pid-list'),
    url(r'^cgroup/(?P<name>\w+)/pid/(?P<pid>[0-9]+)$', CGroupPidView.as_view(), name='pid-modify'),
    url(r'^admin/', admin.site.urls),
]
