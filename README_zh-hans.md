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
    <a href="https://gitee.com/huui/cn-trader/blob/master/LICENSE">
        <img alt="GitHub" src="https://gitee.com/huui/cn-trader/blob/master/static/license.svg?color=blue">
    </a>
</p>

<h4 align="center">
    <p>
        <a href="https://gitee.com/huui/cn-trader/blob/master/README.md">English</a> |
        <b>简体中文</b>
</h4>

## 概述

符合中国市场习惯的金融交易策略回测系统，基于 [backtrader](https://www.backtrader.com) and [AkShare](https://www.akshare.xyz) 。

## 安装

当前代码在以下环境测试通过：
Python 3.10+, backtrader 1.9+ and AkShare 1.4+

### 使用 pip 安装

```bash
pip install cn-trader
```

### 从源码安装

```bash
$ git clone https://github.com/codfish-zz/cn-trader
$ cd cn-trader
$ pip install -r requirements.txt
```

或者

```bash
$ git clone https://gitee.com/huui/cn-trader.git
$ cd cn-trader
$ pip install -r requirements.txt
```

## 快速上手

启动 cn-trader UI 回测已有策略。

```python
>>> from cn_trader import ui
>>> ui.main()
```

> _主菜单_ ![主菜单](https://gitee.com/huui/cn-trader/raw/master/static/main_menu.png)

> _输入证券代码_ ![输入证券代码](https://gitee.com/huui/cn-trader/raw/master/static/input_stock_symbol.png)

> _修改缺省参数值_ ![修改缺省参数值](https://gitee.com/huui/cn-trader/raw/master/static/change_default_params.png)

> _是否绘图_ ![是否绘图](https://gitee.com/huui/cn-trader/raw/master/static/show_picture_or_not.png)

> _是否打印交易日志_ ![是否打印交易日志](https://gitee.com/huui/cn-trader/raw/master/static/show_log_or_not.png)

> _绘图_ ![绘图](https://gitee.com/huui/cn-trader/raw/master/static/plotting_full.png)

> _绘图放大_ ![绘图放大](https://gitee.com/huui/cn-trader/raw/master/static/plotting_section.png)

> _交易日志和回测结果_ ![交易日志和回测结果](https://gitee.com/huui/cn-trader/raw/master/static/show_output.png)

> _菜单自动提示_ ![菜单自动提示](https://gitee.com/huui/cn-trader/raw/master/static/menu_completing.png)

## 测试

运行单个测试用例：

```bash
$ cd tests
$ python -m unittest tests.test_stock_mainland.StockMainlandTestCase.test_strategy_check_sma_cross
```

> _Output_ > ![Output](https://gitee.com/huui/cn-trader/raw/master/static/unit_test_single.png)

运行所有测试用例：

```bash
$ cd tests
$ python -m unittest discover -v
```

> _Output_ > ![Output](https://gitee.com/huui/cn-trader/raw/master/static/unit_test_all.png)
