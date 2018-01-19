# cloud-harmony-test

## Setup

1. After cloning the source code run `pip install -r requirements.txt` to install dependencies
2. Run `sudo user_cgroups {user}` This will only give the user permissions to manage cgroups in his or her own 
    sub-directories and process. Then you need to change `CGROUP_USER={user}` in `cgroup_management.settings.py`. The default is `{user} -> usertest`. Of course, you need to create `usertest` and add it to sudo group.
3. Run `python manage.py test` to run the test
4. Run `python manage.py runserver` to run the web app (default at `http://127.0.0.1:8000/`)

## Usage

To create a new cgroup name
<pre>
POST /cgroup/{cgroupname}
</pre>

To get list of PID in a cgroup
<pre>
GET /cgroup/{cgroupname}/pid
</pre>

To add a PID to a cgroup
<pre>
PUT /cgroup/{cgroupname}/pid/{pid}
</pre>

To remove a PID from a cgroup
<pre>
DELETE /cgroup/{cgroupname}/pid/{pid}
</pre>
