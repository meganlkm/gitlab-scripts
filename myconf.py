#!/usr/bin/python

import unirest, json, os, urllib

def gitlaburl(): return 'https://gitlaburl.com/api/v3/'
def defaultns(): return 'something'

def token():
    mytoken = os.environ.get('GITLAB_TOKEN')

    if not mytoken:
        raise SystemExit('token is not set')

    return mytoken

def urlencode(myurl=None):
    return urllib.quote_plus(myurl)

def urldecode(myurl=None):
    return urllib.unquote_plus(myurl)


# requires unirest
# pip install unirest
# http://unirest.io/python.html

# use git library to initialize repo
# from git import *
# https://pythonhosted.org/GitPython/0.3.1/tutorial.html
