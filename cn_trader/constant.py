from enum import Enum, unique


# https://rich.readthedocs.io/en/latest/style.html
# https://rich.readthedocs.io/en/latest/appendix/colors.html#appendix-colors
class RichColor:
    positive = "bright_red"
    negative = "bright_yellow"


@unique
class Provider(Enum):
    eastMoney = 1
    sina = 2


class PriceAdjust:
    none = "none"
    qfq = "qfq"
    hfq = "hfq"
