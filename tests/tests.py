import unittest
import mock

import wmi_client_wrapper as wmi

class TestCases(unittest.TestCase):
    def test_object_creation():
        wmic = wmi()

if __name__ == "__main__":
    unittest.main()