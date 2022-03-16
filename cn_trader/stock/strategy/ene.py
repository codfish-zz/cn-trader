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
