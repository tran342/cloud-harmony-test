FROM centos:7

RUN yum -y update
RUN DEBIAN_FRONTEND=noninteractive yum install -y git build-essential libtool autoconf automake pkg-config unzip libkrb5-dev default-libmysqlclient-dev

RUN yum  -y install python2.7 python-setuptools python-dev libssl-dev libffi-dev  libxml2-dev libxslt1-dev zlib1g-dev vim locales tmux

RUN curl "https://bootstrap.pypa.io/get-pip.py" -o "get-pip.py"
RUN python get-pip.py

RUN pip install -U pip

EXPOSE 8000

WORKDIR /app

ADD . /app

RUN pip install -r requirements.txt

RUN adduser usertest
RUN passwd -d usertest
RUN usermod -aG wheel usertest

# In order to create those cgroups sub-directories, use the user_cgroups command as root.
RUN su - usertest
RUN user_cgroups usertest

CMD ["python", "/app/src/cgroup_management/manage.py", "runserver", "0.0.0.0:8000"]
