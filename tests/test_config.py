""" Test Config """

from unittest import TestCase

from mygitlab.config import Config


class TestConfig(TestCase):

    """ Test mygitlab.Config """

    def test_init(self):
        """ Init mygitlab """
        cfg = Config()
        self.assertEquals(cfg.get_cfg_val('default_namespace'), 'something')
#         path = self.tmp_repos()
#         name = 'repository_name'
