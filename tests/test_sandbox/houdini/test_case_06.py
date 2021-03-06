# -*- coding: utf-8 -*-
#
# Copyright (c) 2019, Martin Chatterjee. All rights reserved.
# -----------------------------------------------------------------------------

import os
import sys

import vfxtest

# dirty hack
sys.path.append(os.path.dirname(os.path.dirname(os.getcwd())))

import awesome_module

# -----------------------------------------------------------------------------
class TestCase06(vfxtest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    # -------------------------------------------------------------------------
    def test01_(self):

        tr = self.test_root
        self.assertTrue(os.path.exists(tr))
        # retrieve settings in here
        current_context = self.context
        print('    [TestCase06]  current context:          {}'.format(current_context))
        executable = self.context_settings.get('executable', None)
        print('    [TestCase06]  settings executable:      {}'.format(executable))
        print('    [TestCase06]  real executable:          {}'.format(sys.executable))
        print('    [TestCase06]  test_root:                {}'.format(self.test_root))

        foo = awesome_module.hou_internal(3, 5)
        self.assertEqual(foo, 8)

    # -------------------------------------------------------------------------
    def test02_(self):

        foo = awesome_module.hou_internal(6, 4)
        self.assertEqual(foo, 10)

    # -------------------------------------------------------------------------
    def test03_(self):
        foo = awesome_module.hou_internal(1, 2)
        self.assertEqual(foo, 3)
