import unittest

import helloWorld


class TestMethods(unittest.TestCase):
    def test_add(self):
        self.assertEqual(helloWorld.helloWorld(), "hello python sonar")


if __name__ == '__main__':
    unittest.main()
