from tests.base import BaseTestCase
from cn_trader.util import (
    is_number,
    is_stock_symbol,
    is_valid_date,
)


class UtilTestCase(BaseTestCase):
    def setUp(self):
        super(UtilTestCase, self).setUp()

    def test_is_number(self):
        self.assertFalse(is_number(None, 5, 10))
        self.assertFalse(is_number("", 5, 10))
        self.assertFalse(is_number("abc", 5, 10))
        self.assertFalse(is_number("abc3", 5, 10))
        self.assertFalse(is_number("3abc", 5, 10))
        self.assertFalse(is_number("3", 5, 10))
        self.assertTrue(is_number("5", 5, 10))
        self.assertTrue(is_number("10", 5, 10))
        self.assertFalse(is_number("11", 5, 10))

    def test_is_stock_symbol(self):
        self.assertFalse(is_stock_symbol(None))
        self.assertFalse(is_stock_symbol(""))
        self.assertFalse(is_stock_symbol("sh600001"))
        self.assertFalse(is_stock_symbol("sz000001"))
        self.assertFalse(is_stock_symbol("500000"))
        self.assertFalse(is_stock_symbol("6000001"))
        self.assertTrue(is_stock_symbol("000001"))
        self.assertTrue(is_stock_symbol("300368"))
        self.assertTrue(is_stock_symbol("600001"))

    def test_is_valid_date(self):
        self.assertFalse(is_valid_date("1213123"))
        self.assertFalse(is_valid_date(None))
        self.assertFalse(is_valid_date("123"))
        self.assertFalse(is_valid_date("2020-12-01"))
        self.assertFalse(is_valid_date("20201301"))
        self.assertFalse(is_valid_date("20201232"))
        self.assertTrue(is_valid_date("20201201"))
