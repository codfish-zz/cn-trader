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


class Trades(bt.observers.Trades):
    """
    This observer keeps track of full trades and plot the PnL level achieved
    when a trade is closed.

    A trade is open when a position goes from 0 (or crossing over 0) to X and
    is then closed when it goes back to 0 (or crosses over 0 in the opposite
    direction)

    Params:
      - ``pnlcomm`` (default: ``True``)
        Show net/profit and loss, i.e.: after commission. If set to ``False``
        if will show the result of trades before commission

      - ``pnlplus_color`` (default: ``red``)

      - ``pnlminus_color`` (default: ``blue``)
    """

    params = (
        ("pnlcomm", True),
        ("pnlplus_color", "red"),
        ("pnlminus_color", "blue"),
    )

    def __init__(self):
        super(Trades, self).__init__()

        self.plotlines.pnlplus.color = self.params.pnlplus_color
        self.plotlines.pnlminus.color = self.params.pnlminus_color
