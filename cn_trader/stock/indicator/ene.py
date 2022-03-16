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


# 根据价格偏离20日均线的阈值，构建类似于布林带的通道线指标。
class Ene(bt.Indicator):
    lines = ("mid", "top", "bot")
    params = (("maperiod", 20), ("period", 3), ("highRate", 1.2), ("lowRate", 0.85))

    # 与价格在同一张图
    plotinfo = dict(subplot=False)

    def __init__(self):
        super(Ene, self).__init__()

        # 计算上中下轨线
        ema = bt.ind.EMA(self.data, period=self.p.maperiod)
        self.l.mid = bt.ind.EMA(ema, period=self.p.period)
        self.l.top = bt.ind.EMA(self.mid * self.p.highRate, period=self.p.period)
        self.l.bot = bt.ind.EMA(self.mid * self.p.lowRate, period=self.p.period)
