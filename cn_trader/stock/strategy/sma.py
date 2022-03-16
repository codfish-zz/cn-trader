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

import backtrader as bt
from cn_trader.stock.strategy.base import Strategy


class SmaBS(Strategy):
    describe = "收盘价突破均线买入，跌破均线卖出。"

    def __init__(
        self,
        period=20,
        print_log=False,
    ):
        # 调用父类构造函数
        super(SmaBS, self).__init__(
            print_log=print_log,
        )
        self.period = period

        # 指定价格序列
        self.data_close = self.datas[0].close

        # 添加移动均线指标
        self.sma = bt.indicators.SimpleMovingAverage(self.datas[0], period=self.period)

    def next(self):
        # 检查是否有指令等待执行
        if self.order:
            return

        if not self.position:
            # 没有持仓，收盘价格上涨突破均线，买入
            if self.data_close[0] > self.sma[0]:
                self.order = self.buy()
        else:
            # 持有仓位，收盘价格跌破均线，卖出
            if self.data_close[0] < self.sma[0]:
                self.order = self.sell()

    def stop(self):
        """
        回测结束
        """
        self.log(f"均线: {self.period}, 总资金: {self.broker.getvalue():.2f}")


class SmaCross(Strategy):
    describe = "快速均线上穿慢速均线买入，快速均线下穿慢速均线卖出"

    # list of parameters which are configurable for the strategy
    params = (
        ("pfast", 10),  # period for the fast moving average
        ("pslow", 30),  # period for the slow moving average
    )

    def __init__(
        self,
        print_log=False,
    ):
        # 调用父类构造函数
        super(SmaCross, self).__init__(
            print_log=print_log,
        )

        sma1 = bt.ind.SMA(period=self.params.pfast)
        sma2 = bt.ind.SMA(period=self.params.pslow)
        self.crossover = bt.ind.CrossOver(sma1, sma2)

    def next(self):
        # If an order is pending, we cannot send a 2nd one
        if self.order:
            return

        if not self.position:
            # 没有持仓，快速均线上穿慢速均线，买入
            if self.crossover > 0:
                self.order = self.buy()
        else:
            # 持有仓位，快速均线下穿慢速均线，卖出
            if self.crossover < 0:
                self.order = self.close()

    def stop(self):
        """
        回测结束
        """
        self.log(
            f"快速均线: {self.params.pfast}, 慢速均线: {self.params.pslow}, 总资金: {self.broker.getvalue():.2f}"
        )
