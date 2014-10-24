""" gitlab cli config """

from os import environ, path
import yaml

from . import config_file


class Config(object):

    """ Config for mygitlab """

    def __init__(self):
        """ Config::init """
        if config_file == '' or not path.exists(config_file):
            raise SystemExit('Config file is not set or does not exist')
        self._load(config_file)
        self.set_token()

    def _load(self, config_file):
        """ Config::load """
        print "config file: " + config_file
        f = open(config_file)
        self.cfg = yaml.safe_load(f)
        f.close()

    def get_cfg_val(self, key):
        """ Config:::get_cfg_val """
        if key in self.cfg:
            return self.cfg[key]
        else:
            print "key not found..."

    def set_token(self):
        """ Config:::set_token """
        self.token = environ.get('GITLAB_TOKEN')
        if not self.token:
            raise SystemExit('token is not set')

    def token(self):
        """ Config::token """
        return self.token


def main(argv=None):
    """ The console runner function for mygitlab """
    myc = Config()
    myc.get_cfg_val('default_namespace')
    print myc.token
    # CommandLine(prog=prog).main(argv=argv)

if __name__ == '__main__':
    main()
