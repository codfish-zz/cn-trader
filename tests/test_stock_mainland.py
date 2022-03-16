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

import numpy as np
import time
import warnings

from cn_trader.stock.constant import (
    Provider,
    PriceAdjust,
)
from cn_trader.stock.mainland import Mainland
from tests.base import BaseTestCase


class StockMainlandTestCase(BaseTestCase):
    def setUp(self):
        super(StockMainlandTestCase, self).setUp()
        self.mainland = Mainland()

        # Ignore warnings from Matplotlib
        warnings.filterwarnings("ignore")

    def tearDown(self):
        super(StockMainlandTestCase, self).tearDown()

        # Sleep 1 second between AkShare API call.
        time.sleep(1)

    def test_zh_a_hist_daily(self):
        start_date = "20220105"
        end_date = "20220106"
        adjust = PriceAdjust.qfq

        # A股个股历史行情数据（东财）
        # 2022-01-05  16.58  17.15  17.22  16.55  1961998  3.344125e+09  4.02  2.94  0.49  1.01
        # 2022-01-06  17.11  17.12  17.27  17.00  1107885  1.896536e+09  1.57 -0.17 -0.03  0.57
        hist = self.mainland.zh_a_hist_daily(
            Provider.eastMoney, "000001", start_date, end_date, adjust
        )

        columns = [
            "日期",
            "开盘",
            "收盘",
            "最高",
            "最低",
            "成交量",
            "成交额",
            "振幅",
            "涨跌幅",
            "涨跌额",
            "换手率",
        ]
        self.assertEqual(hist.columns.values.tolist(), columns)
        self.assertEqual(hist.values.shape[1], 11, "value size of one row")

        # A股个股历史行情数据（新浪）
        # 2022-01-05  16.58  17.22  16.55  17.15  196199817.0  1.940575e+10  0.010110
        # 2022-01-06  17.11  17.27  17.00  17.12  110788519.0  1.940575e+10  0.005709
        hist = self.mainland.zh_a_hist_daily(
            Provider.sina, "sz000001", start_date, end_date, adjust
        )

        columns = [
            "date",
            "open",
            "high",
            "low",
            "close",
            "volume",
            "outstanding_share",
            "turnover",
        ]
        np.testing.assert_array_equal(hist.columns.values, columns)
        self.assertEqual(hist.values.shape[1], 8, "value size of one row")

    def test_strategy_check_ene(self):
        self.mainland.strategy_check_ene(
            symbol="000002",
            start_date="20210101",
            end_date="20220101",
            show_picture=False,
            print_log=True,
        )

    def test_strategy_check_sma_bs(self):
        self.mainland.strategy_check_sma_bs(
            symbol="000002",
            period=10,
            start_date="20210101",
            end_date="20220101",
            show_picture=False,
            print_log=True,
        )

    def test_strategy_check_sma_cross(self):
        self.mainland.strategy_check_sma_cross(
            symbol="000002",
            start_date="20210901",
            end_date="20220101",
            pfast=5,
            pslow=10,
            adjust=PriceAdjust.qfq,
            show_picture=False,
            print_log=True,
        )
