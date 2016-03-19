# -*- coding: utf-8 -*-

from prod import *

TEST_THIRDPARTY_APPS = [
    'django_nose',
]

INSTALLED_APPS += TEST_THIRDPARTY_APPS

TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

NOSE_ARGS = [
    '--with-coverage',
    '--verbosity=2',
    '--cover-package='+",".join(RAW_APPS)
]