# file: setup.py
"""
MyGitLab

setup.py
"""

from setuptools import setup, find_packages


setup(name='mygitlab',
      version='0.0.3',
      description='gitlab api wrapper',
      author='Megan Wood',
      author_email='megan@devstuff.io',
      packages=find_packages('.', exclude=['examples*', 'test*']),
      tests_require=['coverage', 'green >= 1.7.0', 'mock'],
      test_suite='tests',
      scripts=[],
      entry_points={
          'console_scripts': ['mygitlab = mygitlab.config:main'],
      })
