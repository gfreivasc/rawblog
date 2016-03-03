# -*- coding: utf-8 -*-

from prod import *

THIRDPARTY_APPS = [
    'django_nose',
]

INSTALLED_APPS += THIRDPARTY_APPS

TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

NOSE_ARGS = [
    '--with-coverage',
    '--verbosity=2',
    '--cover-package='+",".join(RAW_APPS)
]