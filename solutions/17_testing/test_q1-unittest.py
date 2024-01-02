import unittest
from shared_test_data import valid_ip_addresses, \
    invalid_ip_address_fields, invalid_ip_address_range, invalid_ip_address_values
from classify import classify_ip


class TestClassifyIp(unittest.TestCase):
    def test_valid_ip_returns_class_type(self):
        for ip, name in valid_ip_addresses:
            with self.subTest(ip=ip, name=name):
                self.assertEqual(classify_ip(ip), name)

    def test_invalid_ip_fields_raises_UserWarning(self):
        for ip in invalid_ip_address_fields:
            with self.subTest(ip=ip):
                with self.assertRaisesRegex(UserWarning, 'four dot'):
                    classify_ip(ip)

    def test_invalid_ip_ranges_raises_UserWarning(self):
        for ip in invalid_ip_address_range:
            with self.subTest(ip=ip):
                with self.assertRaisesRegex(UserWarning, 'Invalid number'):
                    classify_ip(ip)

    def test_invalid_ip_ranges_raises_ValueError(self):
        for ip in invalid_ip_address_values:
            with self.subTest(ip=ip):
                with self.assertRaises(ValueError):
                    classify_ip(ip)
