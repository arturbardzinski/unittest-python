import unittest

def setUpModule():
    print('setting up module ...')

def tearDownModule():
    print('tearing down module ...')

class TestClass1(unittest.TestCase):

    def test_case1(self):
        self.assertEqual('John Smith'.split(),['John', 'Smith'])