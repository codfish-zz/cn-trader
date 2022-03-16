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


class Strategy(bt.Strategy):
    describe = "Base Strategy"
    print_log = False

    def __init__(
        self,
        print_log=False,
    ):
        """
        初始化函数
        """
        self.print_log = print_log

        # 初始化交易指令、买卖价格和手续费
        self.order = None
        self.buyprice = None
        self.buycomm = None

    def next(self):
        """
        主逻辑
        """
        pass

    def notify_order(self, order):
        """
        记录交易执行情况
        """
        if order.status in [order.Submitted, order.Accepted]:
            # Buy/Sell order submitted/accepted to/by broker - Nothing to do
            return

        # Check if an order has been completed
        # Attention: broker could reject order if not enough cash
        if order.status in [order.Completed]:
            price = order.executed.price
            value = order.executed.value
            comm = order.executed.comm

            if order.isbuy():
                self.log(f"买入: (价格: {price:.2f}, 成本: {value:.2f}, 手续费: {comm:.2f})")
                self.buyprice = price
                self.buycomm = comm
            elif order.issell():
                self.log(f"卖出: (价格: {price:.2f}, 成本: {value:.2f}, 手续费: {comm:.2f})")

            self.bar_executed = len(self)
        elif order.status in [order.Canceled, order.Margin, order.Rejected]:
            self.log("交易失败")

        # No pending order
        self.order = None

    def notify_trade(self, trade):
        """
        记录交易收益情况
        """
        if trade.isclosed:
            self.log(f"策略收益: (毛收益: {trade.pnl:.2f}, 净收益: {trade.pnlcomm:.2f})")

    def stop(self):
        """
        回测结束
        """
        self.log(f"总资金: {self.broker.getvalue():.2f}")

    def log(self, txt):
        if self.print_log:
            dt = self.datas[0].datetime.date(0)
            print("[%s] %s" % (dt.isoformat(), txt))
