from django.conf import settings
from cgroups import Cgroup
from cgroups.common import CgroupsException
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.exceptions import APIException, ValidationError


def get_or_create_cgroup(name):
    try:
        cg = Cgroup(name, user=settings.CGROUP_USER)
    except Exception:
        raise APIException(detail='Cgroup error.')

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

    def get(self, request, name, pid):
        cg = get_or_create_cgroup(name)

        if pid:
            pid = int(pid)
            if pid in cg.pids:
                return Response([pid])

        return Response(cg.pids)

    def put(self, request, name, pid):
        cg = get_or_create_cgroup(name)

        pid = int(pid)
        try:
            cg.add(pid)
        except CgroupsException:
            raise ValidationError(detail='Pid %s does not exists.' % pid)
        except Exception:
            raise APIException(detail='Not able to add new PID.')

        return Response(pid)

    def delete(self, request, name, pid):
        cg = get_or_create_cgroup(name)

        pid = int(pid)
        try:
            cg.remove(pid)
        except CgroupsException:
            raise ValidationError(detail='Pid %s does not exists.' % pid)
        except Exception:
            raise APIException(detail='Not able to remove Pid.')

        return Response(True)
