#!/usr/bin/python

import sys, getopt, myconf, unirest, json, urllib

def usage():
    raise SystemExit('Usage: get-project {-p <project_name> | -i <project_id>} [-n <project_namespace>]')

if 2 > len(sys.argv):
    usage()

argv = sys.argv[1:]

if not argv:
    usage()

myopts = "n:p:i:"
opts, args = getopt.getopt(argv, myopts)

if 1 > len(opts):
    usage()

project_namespace = myconf.defaultns()
project_id = 0

for opt, val in opts:
    if opt == '-h':
        usage()
    elif opt == "-n":
        project_namespace = val
    elif opt == "-p":
        project_id = project_namespace + '/' + val
    elif opt == "-i":
        project_id = val

project_id = myconf.urlencode(project_id)

url = myconf.gitlaburl() + 'projects/' + project_id
resp = unirest.get(url, headers={"PRIVATE-TOKEN": myconf.token()})
project_data = json.loads(resp.raw_body)
print json.dumps(project_data, sort_keys=True, indent=4, separators=(',', ': '))
