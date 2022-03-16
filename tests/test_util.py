# coding=utf-8
# Copyright 2020-present, BigFish (huui1998@163.com).
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from tests.base import BaseTestCase
from cn_trader.stock.util import (
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
