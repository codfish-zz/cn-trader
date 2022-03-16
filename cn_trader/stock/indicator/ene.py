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
