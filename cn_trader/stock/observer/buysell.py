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
