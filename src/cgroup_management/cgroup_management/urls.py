from django.conf.urls import url
from django.contrib import admin

from cgroup_management.views import CGroupPidView, CGroupView

urlpatterns = [
    url(r'^cgroup/(?P<name>\w+)$', CGroupView.as_view()),
    url(r'^cgroup/(?P<name>\w+)/pid$', CGroupPidView.as_view()),
    url(r'^cgroup/(?P<name>\w+)/pid/(?P<pid>[0-9]+)$', CGroupPidView.as_view()),
    url(r'^admin/', admin.site.urls),
]
