from django.conf import settings
from cgroups.common import CgroupsException
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.exceptions import APIException

from cgroups import Cgroup


def get_or_create_cgroup(name):
    try:
        cg = Cgroup(name, settings.CGROUP_USER)
    except Exception:
        # raise APIException(detail='Cgroup error.')
        raise
    return cg


class CGroupView(APIView):
    parser_classes = (JSONParser,)

    def post(self, request, name):
        get_or_create_cgroup(name)
        return Response({'Name': name})

    def delete(self, request, name):
        try:
            cg = Cgroup(name)
            cg.delete()
        except Exception:
            raise APIException(detail='Not able to delete Cgroup.')

        return Response(True)


class CGroupPidView(APIView):
    parser_classes = (JSONParser,)

    def get(self, request, name):
        try:
            cg = Cgroup(name)
        except Exception:
            raise APIException(detail='Cgroup error.')

        return Response(cg.pids)

    def post(self, request, name, pid):
        try:
            cg = Cgroup(name)
        except Exception:
            raise APIException(detail='Cgroup error.')

        try:
            cg.add(pid)
        except CgroupsException:
            raise APIException(detail='Pid %s does not exists.' % pid)
        except Exception:
            raise APIException(detail='Not able to add new PID.')

        return Response({
            'Name': name,
            'Pid': pid
        })

    def delete(self, request, name, pid):
        try:
            cg = Cgroup(name)
        except Exception:
            raise APIException(detail='Cgroup error.')

        try:
            cg.remove(pid)
        except CgroupsException:
            raise APIException(detail='Pid %s does not exists.' % pid)
        except Exception:
            raise APIException(detail='Not able to remove Pid.')

        return Response(True)
