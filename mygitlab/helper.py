""" gitlab helper """

import urllib


def urlencode(myurl=None):
    """ helper.urlencode """
    return urllib.quote_plus(myurl)


def urldecode(myurl=None):
    """ helper.urldecode """
    return urllib.unquote_plus(myurl)
