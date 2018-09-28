import unittest

import myapp


class MyappTest(unittest.TestCase):
	def test_hello(self):
		assert myapp.hello() == 'Hello World!'
