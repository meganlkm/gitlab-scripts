#!/usr/bin/python

import inspect, os, myconf, unirest, json

url = myconf.gitlaburl() + 'user'

resp = unirest.get(url, headers={"PRIVATE-TOKEN": myconf.token()})
print json.dumps(resp.body, sort_keys=True, indent=4, separators=(',', ': '))
