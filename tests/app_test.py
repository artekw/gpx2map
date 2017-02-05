#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import unittest

topdir = os.path.join(os.path.dirname(__file__), "..")
sys.path.append(topdir)
import gpx2map



class Gpx2osmTest(unittest.TestCase):
    '''Test app'''


    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        # creates a test client
        self.app = gpx2map.app.test_client()
        # propagate the exceptions to the test client
        self.app.testing = True

    def tearDown(self):
        pass

    def test_home_status_code(self):
        '''Test home'''
        # sends HTTP GET request to the application
        # on the specified path
        result = self.app.get('/')

        # assert the status code of the response
        self.assertEqual(result.status_code, 200)
'''
    def test_home_data(self):
        # sends HTTP GET request to the application
        # on the specified path
        result = self.app.get('/') 

        # assert the response data
        self.assertEqual(result.data, "Hello World!!!")
'''

if __name__ == '__main__':
    unittest.main()
