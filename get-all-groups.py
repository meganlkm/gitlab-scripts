#!/usr/bin/python

import inspect, sys, myconf, unirest, json

url = myconf.gitlaburl() + 'groups'
if 1 < len(sys.argv):
    url += '/' + sys.argv[1] # has to be number

resp = unirest.get(url, headers={"PRIVATE-TOKEN": myconf.token()})
# print json.dumps(resp.body, sort_keys=True, indent=4, separators=(',', ': '))
project_data = json.loads(resp.raw_body)
# print json.dumps(project_data, sort_keys=True, indent=4, separators=(',', ': '))

print json.dumps(project_data[0], sort_keys=True, indent=4, separators=(',', ': '))

print project_data[0]['id']
