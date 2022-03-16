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
import cn_trader.stock.indicator as ind
from cn_trader.stock.strategy.base import Strategy


class Ene(Strategy):
    describe = "收盘价站在Ene中轨线上，且成交量突破20日新高时买入，收盘价突破Ene上轨线卖出。"
    params = (("period", 20),)

    def __init__(
        self,
        print_log=False,
    ):
        # 调用父类构造函数
        super(Ene, self).__init__(
            print_log=print_log,
        )

        self.order = None
        self.mid = ind.Ene(self.data).mid
        self.top = ind.Ene(self.data).top
        self.bot = ind.Ene(self.data).bot

        # 设置买入信号
        self.buy_sig = bt.And(
            self.data.close > self.mid,
            self.data.volume == bt.ind.Highest(self.data.volume, period=self.p.period),
        )

        # 卖出信号
        self.sell_sig = self.data.close > self.top

    def next(self):
        if not self.position:
            if self.buy_sig:
                self.order = self.buy()
        else:
            if self.sell_sig:
                self.order = self.sell()
