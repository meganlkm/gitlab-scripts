#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
run_tests.py

configure environment for unit testing
"""

import unittest
import sys

# from green.suite import GreenTestSuite
from green.config import default_args
from green.loader import loadTargets, loadFromTestCase
from green.output import GreenStream
from green.runner import run
from green.suite import GreenTestSuite

# Import Test Suite Classes
from tests.test_config import TestConfig
# from tests import test_migrations
# from tests.manager_site_tests import ManagerSiteTest
# from tests.myapp_unittests import MyAppUnitTest

# Track Code Coverage Report
# from coverage import coverage
# cov = coverage(branch=True,
#                source=['mygitlab'])
#                # omit=['env/*', 'run_tests.py', 'tests/*'])
# cov.start()


# Returns a TestSuite for all the test classes we want to run
def suite():
    """ return our TestSuite """
    suite = GreenTestSuite()
    suite = loadFromTestCase(TestConfig)
    return suite


def getargs():
    """ return arguments for green """
    ga = copy.deepcopy(default_args)
    ga.verbose = 3
    ga.run_coverage = True
    ga.completions = True
    ga.logging = True
    return ga
#     targets=['.'],  # Not in configs
#     subprocesses=1,
#     html=False,
#     termcolor=None,
#     notermcolor=None,
#     allow_stdout=False,
#     debug=0,
#     help=False,  # Not in configs
#     logging=False,
#     version=False,
#     verbose=1,
#     failfast=False,
#     config=None,  # Not in configs
#     run_coverage=False,
#     omit=None,
#     completion_file=False,
#     completions=False,
#     options=False,
#     # These are not really options, they are added later for convenience
#     parser=None,
#     store_opt=None,
#     # not implemented, but unittest stub in place
#     warnings='',

# If we run from the command line directly, run the test suite
if __name__ == '__main__':
    run(suite(),
        sys.stdout,
        getargs())
