#!/usr/bin/python

import sys, os, shutil, getopt
import unirest, json
import myconf

# from git import *
# https://pythonhosted.org/GitPython/0.3.1/tutorial.html

script_name = __file__

def usage():
    raise SystemExit('Usage: ' + script_name + ' -p <project_name> [-d <project_desc>] [-n <project_namespace>]')

# # usage() {
# #     echo "${txtbld}Usage:${txtrst}"
# #     echo "  ${SCRIPT_NAME} {-p} [options]"
# #     echo "${txtbld}Options:${txtrst}"
# #     echo "  -p project_name"
# #     echo "  -n namespace_id :: namespace for the new project (defaults to ${ns})"
# #     echo "  -d description :: short project description"
# #     # echo "  -i :: issues_enabled"
# #     # echo "  -m :: merge_requests_enabled"
# #     # echo "  -w :: wiki_enabled"
# #     # echo "  -s :: snippets_enabled"
# #     # echo "  -p :: public"
# #     # echo "  -v :: visibility_level"
# #     # echo "  -u url :: import_url"
# #     exit 1
# # }

def get_group(grp_name):
    url = myconf.gitlaburl() + 'groups'
    groups_resp = unirest.get(url, headers={"PRIVATE-TOKEN": myconf.token()}) # need to cache this
    group_data = json.loads(groups_resp.raw_body)
    for group in group_data:
        if group['name'] == grp_name:
            return group['id']
    return False

if 2 > len(sys.argv):
    usage()

argv = sys.argv[1:]

myopts = "hn:p:d:"
opts, args = getopt.getopt(argv, myopts)

if 1 > len(opts):
    usage()

project_namespace = myconf.defaultns()
project_name = ''
project_desc = ''

for opt, val in opts:
    if opt == '-h':
        usage()
    elif opt == "-n":
        project_namespace = val
    elif opt == "-p":
        project_name = val
    elif opt == "-d":
        project_desc = val

project_namespace = get_group(project_namespace)
url = myconf.gitlaburl() + 'projects'
url_data = {
    'name': project_name,
    'namespace_id': project_namespace,
    'description': project_desc
}

# # # name (required) - new project name
# # # namespace_id (optional) - namespace for the new project (defaults to user)
# # # description (optional) - short project description
# # # issues_enabled (optional)
# # # merge_requests_enabled (optional)
# # # wiki_enabled (optional)
# # # snippets_enabled (optional)
# # # public (optional) - if true same as setting visibility_level = 20
# # # visibility_level (optional)
# # # import_url (optional)

create_resp = unirest.post(url, headers={"PRIVATE-TOKEN": myconf.token()}, params = url_data)
# print json.dumps(resp.body, sort_keys=True, indent=4, separators=(',', ': '))
project_data = json.loads(create_resp.raw_body)
project_id = project_data['id']

print project_id

# basedir = os.getcwd()
# tmpdir = basedir + '/newtmp'

## create tmpdir if it does not exist
# if not os.path.exists(tmpdir):
#     os.makedirs(tmpdir)

#############################
# use git lib for this...
# https://pythonhosted.org/GitPython/0.3.1/tutorial.html
# # tmpdir=${BASE_DIR}/tmp
# # mkdir -p ${tmpdir}/${project} && cd ${tmpdir}/${project}
# # git init
# # touch README
# # git add README
# # git commit -m 'initial commit'
# # git remote add origin git@gitlaburl.com:${ns}/${project}.git
# # git push -u origin master
# # git checkout -b develop origin/master
# # git push origin develop
#############################

## remove tmpdir
# shutil.rmtree(tmpdir, ignore_errors=True)

## protect master branch
# url = myconf.gitlaburl() + 'projects/' + project_id + '/repository/branches/master/protect'
# protect_resp = unirest.put(url, headers={"PRIVATE-TOKEN": myconf.token()})
# print json.dumps(protect_resp.body, sort_keys=True, indent=4, separators=(',', ': '))


print "Project [" + project_name + " (" + project_id + ")] has been created. Login to gitlab and set the default branch to develop"

#############
## this is the response from creating a project
# {'namespace_id': 85, 'name': 'thisisatest', 'description': ''}
# {
#     "archived": false,
#     "created_at": "2014-10-08T17:56:32.182Z",
#     "default_branch": null,
#     "description": null,
#     "http_url_to_repo": "https://gitlaburl.com/something/thisisatest.git",
#     "id": 178,
#     "issues_enabled": true,
#     "last_activity_at": "2014-10-08T17:56:32.182Z",
#     "merge_requests_enabled": true,
#     "name": "thisisatest",
#     "name_with_namespace": "something / thisisatest",
#     "namespace": {
#         "avatar": {
#             "url": null
#         },
#         "created_at": "2014-08-13T20:46:28.185Z",
#         "description": "",
#         "id": 85,
#         "name": "something",
#         "owner_id": null,
#         "path": "something",
#         "updated_at": "2014-08-13T20:46:28.185Z"
#     },
#     "path": "thisisatest",
#     "path_with_namespace": "something/thisisatest",
#     "public": false,
#     "snippets_enabled": false,
#     "ssh_url_to_repo": "git@gitlaburl.com:something/thisisatest.git",
#     "visibility_level": 0,
#     "web_url": "https://gitlaburl.com/something/thisisatest",
#     "wiki_enabled": true
# }
