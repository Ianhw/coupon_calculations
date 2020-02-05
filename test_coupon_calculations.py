import unittest
import unittest.mock as mock
from store import coupon_calculations


class MyTestCase(unittest.TestCase):

    def test_price_under_ten(self):
        with mock.patch('builtins.input', side_effect=[10, 5, 10]):
            assert coupon_calculations.calculate_order() == 10.45

    def test_price_under_ten2(self):
        with mock.patch('builtins.input', side_effect=[10, 5, 15]):
            assert coupon_calculations.calculate_order() == 10.2

    def test_price_under_ten3(self):
        with mock.patch('builtins.input', side_effect=[10, 5, 20]):
            assert coupon_calculations.calculate_order() == 9.95

    def test_price_under_ten4(self):
        with mock.patch('builtins.input', side_effect=[10, 10, 20]):
            assert coupon_calculations.calculate_order() == 5.95

    def test_price_under_ten4(self):
        with mock.patch('builtins.input', side_effect=[10, 10, 20]):
            assert coupon_calculations.calculate_order() == 5.95

    def test_price_under_between_ten_thirty(self):
        with mock.patch('builtins.input', side_effect=[40, 5, 10]):
            assert coupon_calculations.calculate_order() == 43.45

    def test_price_under_over_fifty(self):
        with mock.patch('builtins.input', side_effect=[50, 5, 10]):
            assert coupon_calculations.calculate_order() == 52.45


if __name__ == '__main__':
    unittest.main()
