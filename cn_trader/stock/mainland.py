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

import akshare as ak
import backtrader as bt
import cn_trader as trader
import matplotlib.pyplot as plt
import os
import pandas as pd
from cn_trader.stock.constant import (
    RichColor,
    Provider,
    PriceAdjust,
)
from datetime import datetime
from rich.console import Console


# 中国大陆证券市场分析回测
class Mainland:
    def __init__(self):
        self.max_rank = int(os.getenv("MAX_RANK", 3))
        self.console = Console()

        # 缺省回测参数
        dt_end_date = datetime.today()
        dt_start_date = datetime(
            dt_end_date.year - 5,
            dt_end_date.month,
            dt_end_date.day,
        )
        self.params = {
            "dt_start_date": dt_start_date,
            "dt_end_date": dt_end_date,
            "start_date": dt_start_date.strftime("%Y%m%d"),
            "end_date": dt_end_date.strftime("%Y%m%d"),
        }

        # 正确显示中文和负号
        plt.rcParams["font.sans-serif"] = ["SimHei"]
        plt.rcParams["axes.unicode_minus"] = False

    def get_stock_data(self, symbol, start_date, end_date, adjust):
        # datatime object
        dt_start_date = None
        dt_end_date = None

        try:
            if start_date is None:
                dt_start_date = self.params["dt_start_date"]
                start_date = self.params["start_date"]
            else:
                dt_start_date = datetime.strptime(start_date, "%Y%m%d")

            if end_date is None:
                dt_end_date = self.params["dt_end_date"]
                end_date = self.params["end_date"]
            else:
                dt_end_date = datetime.strptime(end_date, "%Y%m%d")

        except:
            self.console.print("信息提示: [%s]请按正确格式输入开始和结束日期" % RichColor.negative)
            return None

        if dt_end_date < dt_start_date:
            self.console.print(
                "信息提示: [%s]%s <= %s " % (RichColor.negative, end_date, start_date)
            )
            return None

        hist = self.zh_a_hist_daily(
            Provider.eastMoney,
            symbol,
            start_date,
            end_date,
            adjust,
        )

        if len(hist) == 0:
            self.console.print("信息提示: [%s]未获取到有效数据，请输入正确证券代码。" % RichColor.negative)
            return None

        # 取前6列数据
        stock_df = hist.iloc[:, :6]

        # 处理字段命名，以符合 Backtrader 要求
        stock_df.columns = [
            "date",
            "open",
            "close",
            "high",
            "low",
            "volume",
        ]

        # 把 date 作为日期索引，以符合 Backtrader 的要求
        stock_df.index = pd.to_datetime(stock_df["date"])

        pandas_data = bt.feeds.PandasData(
            dataname=stock_df,
            fromdate=dt_start_date,
            todate=dt_end_date,
        )

        return (stock_df, pandas_data)

    def get_strategy_data(self, strategy, symbol, start_date, end_date, adjust):
        self.console.rule("策略回测 - [%s]" % strategy.describe)

        (stock_df, pandas_data) = self.get_stock_data(
            symbol, start_date, end_date, adjust
        )

        return pandas_data

    def run_strategy(
        self, strategy, data, start_cash, commission, percent_sizer, **kwargs
    ):
        cerebro = bt.Cerebro(stdstats=False)

        cerebro.addobserver(bt.observers.Broker)
        cerebro.addobserver(trader.stock.observer.Trades)
        cerebro.addobserver(trader.stock.BuySell, barplot=True)

        cerebro.addstrategy(strategy, **kwargs)
        cerebro.adddata(data)

        cerebro.broker.setcash(start_cash)
        cerebro.broker.setcommission(commission)

        # 设置买入数量（按仓位百分比计算）
        cerebro.addsizer(bt.sizers.PercentSizer, percents=percent_sizer)

        # 运行回测，获取回测结束后的总资金
        cerebro.run()
        end_cash = cerebro.broker.getvalue()

        return (cerebro, end_cash)

    def show_strategy_result(
        self,
        symbol,
        start_date,
        end_date,
        commission,
        percent_sizer,
        start_cash,
        end_cash,
        show_picture,
        cerebro,
    ):
        profit = end_cash - start_cash

        self.console.print("证券代码: %s" % symbol)
        self.console.print("回测期间: %s - %s" % (start_date, end_date))
        self.console.print("交易量: %d%%" % percent_sizer)
        self.console.print("费率: %.2f%%" % (commission * 100))
        self.console.print("初始资金: %.2f" % start_cash)
        self.console.print("总资金: %.2f" % round(end_cash, 2))
        self.console.print("净收益: %.2f" % round(profit, 2))
        self.console.print("收益率: %.2f%%" % round((profit / start_cash) * 100, 2))

        # 日线图
        # https://rich.readthedocs.io/en/latest/appendix/colors.html#appendix-colors
        if show_picture:
            cerebro.plot(
                grid=False,
                style="candle",
                barup="#d70000",  # red3
                bardown="#005f00",  # dark_green
                barupfill=True,
                bardownfill=True,
                volup="#ffaf5f",  # sandy_brown
                voldown="#87af87",  # dark_sea_green
                voloverlay=False,
            )

    def strategy_check_ene(
        self,
        symbol="000002",
        start_date=None,
        end_date=None,
        adjust=PriceAdjust.qfq,
        start_cash=1000000,
        commission=0.002,
        percent_sizer=90,
        show_picture=False,
        print_log=False,
    ):
        strategy = trader.stock.strategy.Ene
        data = self.get_strategy_data(strategy, symbol, start_date, end_date, adjust)

        if data is None:
            return

        (cerebro, end_cash) = self.run_strategy(
            strategy,
            data,
            start_cash,
            commission,
            percent_sizer,
            print_log=print_log,
        )

        self.show_strategy_result(
            symbol,
            start_date,
            end_date,
            commission,
            percent_sizer,
            start_cash,
            end_cash,
            show_picture,
            cerebro,
        )

    def strategy_check_sma_bs(
        self,
        symbol="000002",
        period=20,
        start_date=None,
        end_date=None,
        adjust=PriceAdjust.qfq,
        start_cash=1000000,
        commission=0.002,
        percent_sizer=50,
        show_picture=False,
        print_log=False,
    ):
        strategy = trader.stock.strategy.SmaBS
        data = self.get_strategy_data(strategy, symbol, start_date, end_date, adjust)

        if data is None:
            return

        (cerebro, end_cash) = self.run_strategy(
            strategy,
            data,
            start_cash,
            commission,
            percent_sizer,
            period=period,
            print_log=print_log,
        )

        self.show_strategy_result(
            symbol,
            start_date,
            end_date,
            commission,
            percent_sizer,
            start_cash,
            end_cash,
            show_picture,
            cerebro,
        )

    def strategy_check_sma_cross(
        self,
        symbol="000002",
        start_date=None,
        end_date=None,
        pfast=10,
        pslow=30,
        adjust=PriceAdjust.qfq,
        start_cash=1000000,
        commission=0.002,
        percent_sizer=50,
        show_picture=False,
        print_log=False,
    ):
        strategy = trader.stock.strategy.SmaCross
        data = self.get_strategy_data(strategy, symbol, start_date, end_date, adjust)

        if data is None:
            return

        (cerebro, end_cash) = self.run_strategy(
            strategy,
            data,
            start_cash,
            commission,
            percent_sizer,
            pfast=pfast,
            pslow=pslow,
            print_log=print_log,
        )

        self.show_strategy_result(
            symbol,
            start_date,
            end_date,
            commission,
            percent_sizer,
            start_cash,
            end_cash,
            show_picture,
            cerebro,
        )

    # A股个股历史行情数据
    def zh_a_hist_daily(self, provider, symbol, start_date, end_date, adjust):
        hist = None

        if provider == Provider.eastMoney:
            hist = ak.stock_zh_a_hist(
                symbol=symbol,
                period="daily",
                start_date=start_date,
                end_date=end_date,
                adjust=adjust,
            )

        if provider == Provider.sina:
            hist = ak.stock_zh_a_daily(
                symbol=symbol,
                start_date=start_date,
                end_date=end_date,
                adjust=adjust,
            )

        return hist
