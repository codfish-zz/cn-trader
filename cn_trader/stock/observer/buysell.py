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


class BuySell(bt.observers.BuySell):
    """
    This observer keeps track of the individual buy/sell orders (individual
    executions) and will plot them on the chart along the data around the
    execution price level

    Params:
      - ``barplot`` (default: ``False``) Plot buy signals below the minimum and
        sell signals above the maximum.

        If ``False`` it will plot on the average price of executions during a
        bar

      - ``bardist`` (default: ``0.015`` 1.5%) Distance to max/min when
        ``barplot`` is ``True``

      - ``buy_color`` (default: ``#d7af00``)

      - ``sell_color`` (default: ``blue``)
    """

    params = (
        ("barplot", False),  # plot above/below max/min for clarity in bar plot
        ("bardist", 0.015),  # distance to max/min in absolute perc
        ("buy_color", "#d7af00"),
        ("sell_color", "blue"),
    )

    def __init__(self):
        super(BuySell, self).__init__()

        self.plotlines.buy.color = self.params.buy_color
        self.plotlines.sell.color = self.params.sell_color
