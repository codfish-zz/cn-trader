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
        <img alt="GitHub" src="https://huui1998.pythonanywhere.com/admin/uploads/cn-trader/license.svg?color=blue">
    </a>
</p>

<h4 align="center">
    <p>
        <a href="https://github.com/codfish-zz/cn-trader/blob/master/README.md">English</a> |
        <b>简体中文</b>
</h4>

## 概述

符合中国市场习惯的金融交易策略回测系统，基于 [backtrader](https://www.backtrader.com) 和 [AkShare](https://www.akshare.xyz) 。

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

> _主菜单_ ![主菜单](https://pic.imgdb.cn/item/6266e5e6239250f7c5a66a50.png)

> _输入证券代码_ ![输入证券代码](https://pic.imgdb.cn/item/6266e59a239250f7c5a60b03.png)

> _修改缺省参数值_ ![修改缺省参数值](https://pic.imgdb.cn/item/6266e59a239250f7c5a60aff.png)

> _是否绘图_ ![是否绘图](https://pic.imgdb.cn/item/6266e5ef239250f7c5a67631.png)

> _是否打印交易日志_ ![是否打印交易日志](https://pic.imgdb.cn/item/6266e5e6239250f7c5a66a7b.png)

> _绘图_ ![绘图](https://pic.imgdb.cn/item/6266e5e6239250f7c5a66a68.png)

> _绘图放大_ ![绘图放大](https://pic.imgdb.cn/item/6266e5e6239250f7c5a66a72.png)

> _交易日志和回测结果_ ![交易日志和回测结果](https://pic.imgdb.cn/item/6266e5ef239250f7c5a6762c.png)

> _菜单自动提示_ ![菜单自动提示](https://pic.imgdb.cn/item/6266e5e6239250f7c5a66a58.png)

## 测试

运行单个测试用例：

```bash
$ cd tests
$ python -m unittest tests.test_stock_mainland.StockMainlandTestCase.test_strategy_check_sma_cross
```

> _Output_ > ![Output](https://pic.imgdb.cn/item/6266e5ef239250f7c5a6763b.png)

运行所有测试用例：

```bash
$ cd tests
$ python -m unittest discover -v
```

> _Output_ > ![Output](https://pic.imgdb.cn/item/6266e5ef239250f7c5a67635.png)
