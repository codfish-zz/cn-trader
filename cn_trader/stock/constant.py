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
