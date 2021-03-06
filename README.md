<!---
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
-->

<h1 align="center">
    <p>cn-trader</p>
</h1>

<p align="center">
    <a href="https://github.com/codfish-zz/cn-trader/blob/master/LICENSE">
        <img alt="license.png" src="https://huui1998.pythonanywhere.com/admin/uploads/cn-trader/license.svg?color=blue">
    </a>
</p>

<h4 align="center">
    <p>
        <b>English</b> |
        <a href="https://github.com/codfish-zz/cn-trader/blob/master/README_zh-hans.md">简体中文</a>
</h4>

## Overview

Python back testing system for trading strategies, based on [backtrader](https://www.backtrader.com) and [AkShare](https://www.akshare.xyz), customized for China market.

## Installation

This repository is tested on Python 3.10+, backtrader 1.9+ and AkShare 1.4+.

### With pip

```bash
pip install cn-trader
```

### With source

```bash
$ git clone https://github.com/codfish-zz/cn-trader
$ cd cn-trader
$ pip install -r requirements.txt
```

Or

```bash
$ git clone https://gitee.com/huui/cn-trader.git
$ cd cn-trader
$ pip install -r requirements.txt
```

## Quick tour

Run cn-trader with UI interface.

```python
>>> from cn_trader import ui
>>> ui.main()
```

> _Main menu_ ![Main menu](https://pic.imgdb.cn/item/6266e5e6239250f7c5a66a50.png)

> _Input stock symbol_ ![Input stock symbol](https://pic.imgdb.cn/item/6266e59a239250f7c5a60b03.png)

> _Change default parameters_ ![Change default parameters](https://pic.imgdb.cn/item/6266e59a239250f7c5a60aff.png)

> _Show picture or not_ ![Show picture or not](https://pic.imgdb.cn/item/6266e5ef239250f7c5a67631.png)

> _Show log or not_ ![Show log or not](https://pic.imgdb.cn/item/6266e5e6239250f7c5a66a7b.png)

> _Full picture_ ![Full picture](https://pic.imgdb.cn/item/6266e5e6239250f7c5a66a68.png)

> _Zoom the picture_ ![Zoom the picture](https://pic.imgdb.cn/item/6266e5e6239250f7c5a66a72.png)

> _Show log and summary_ ![Show log and summary](https://pic.imgdb.cn/item/6266e5ef239250f7c5a6762c.png)

> _Menu auto-completing_ ![Menu auto-completing](https://pic.imgdb.cn/item/6266e5e6239250f7c5a66a58.png)

## Testing

Run single test case.

```bash
$ cd tests
$ python -m unittest tests.test_stock_mainland.StockMainlandTestCase.test_strategy_check_sma_cross
```

> _Output_ ![Output](https://pic.imgdb.cn/item/6266e5ef239250f7c5a6763b.png)

Run all test cases.

```bash
$ cd tests
$ python -m unittest discover -v
```

> _Output_ ![Output](https://pic.imgdb.cn/item/6266e5ef239250f7c5a67635.png)

## Create new strategy

Coming soon...
