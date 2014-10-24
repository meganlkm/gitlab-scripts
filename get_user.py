#!/usr/bin/python
""" get_user.py """

from json import dumps
from unirest import get

from config import Config

cfg = Config()
url = cfg.get(gitlaburl) + 'user'

resp = get(url, headers={"PRIVATE-TOKEN": myconf.token()})
print dumps(resp.body, sort_keys=True, indent=4, separators=(',', ': '))
