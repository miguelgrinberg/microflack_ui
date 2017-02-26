#!/usr/bin/env python
import os
import unittest

from microflack_common.test import FlackTestCase

os.environ['FLASK_CONFIG'] = 'test'
from app import app


class UITests(FlackTestCase):
    def setUp(self):
        self.ctx = app.app_context()
        self.ctx.push()
        self.client = app.test_client()

    def tearDown(self):
        self.ctx.pop()

    def test_index_page(self):
        r, s, h = self.get('/')
        self.assertTrue(h['Content-Type'].startswith('text/html'))


if __name__ == '__main__':
    unittest.main(verbosity=2)
