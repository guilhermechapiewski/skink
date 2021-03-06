#!/usr/bin/env python
#-*- coding:utf-8 -*-
import sys
from os.path import dirname, abspath, join
import unittest
root_path = abspath(join(dirname(__file__), "../../"))
sys.path.insert(0, root_path)

from tests.base.base_unit_test import BaseUnitTest
from tests.imports import *
from skink.plugins import Plugin
from skink.plugins.email_plugin import EmailPlugin

class TestEmailPlugin(BaseUnitTest):
        
    def test_null_configuration(self):
        self.assertRaises(ValueError,EmailPlugin,{"enabled":True})
        self.assertRaises(ValueError,EmailPlugin,{"enabled":True, "smpt_host":"127.0.0.1"})

    def test_disabled_not_raises(self):
        e = EmailPlugin({"enabled":False})
        self.assertNotEquals(e,None)

if __name__ == '__main__':
    unittest.main()
