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

import warnings
import cn_trader as trader

from cn_trader.stock.mainland import Mainland
from cn_trader.stock.util import is_number, is_stock_symbol, is_valid_date
from prompt_toolkit import PromptSession
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.cursor_shapes import CursorShape
from prompt_toolkit.shortcuts import (
    checkboxlist_dialog,
    input_dialog,
    radiolist_dialog,
    yes_no_dialog,
)
from prompt_toolkit.shortcuts import radiolist_dialog
from prompt_toolkit.styles import Style


completer = WordCompleter(
    [
        "exit",
        "stock_mainland_strategy_check",
        "stock_mainland_strategy_check_ene",
        "stock_mainland_strategy_check_sma_bs",
        "stock_mainland_strategy_check_sma_cross",
        "quit",
    ],
    ignore_case=True,
)

prompt_style = Style.from_dict(
    {
        # User input (default text).
        "": "red",
        # Prompt.
        "path": "ansicyan italic",
        "mark": "ansicyan italic",
    }
)

prompt_caption = [
    ("class:path", "cn-trader"),
    ("class:mark", "> "),
]

mainland = Mainland()


def main():
    session = PromptSession(completer=completer)
    current_choice = "stock_mainland_strategy_check"
    last_choice = current_choice

    warnings.filterwarnings("ignore")

    while True:
        if current_choice is None:
            current_choice = last_choice
        else:
            if current_choice == "stock_mainland_strategy_check":
                current_choice = show_stock_mainland_strategy_check()
                continue
            elif current_choice == "stock_mainland_strategy_check_ene":
                show_stock_mainland_strategy_check_ene(session)
            elif current_choice == "stock_mainland_strategy_check_sma_bs":
                show_stock_mainland_strategy_check_sma_bs(session)
            elif current_choice == "stock_mainland_strategy_check_sma_cross":
                show_stock_mainland_strategy_check_sma_cross(session)
            elif current_choice.lower() in ["quit", "exit"]:
                break

        try:
            text = session.prompt(
                prompt_caption,
                style=prompt_style,
                default=current_choice,
                cursor=CursorShape.BLINKING_UNDERLINE,
                mouse_support=True,
            )
        except KeyboardInterrupt:
            break
        except EOFError:
            break

        last_choice = current_choice
        current_choice = text

    print("GoodBye!\n")


def show_stock_mainland_strategy_check():
    result = radiolist_dialog(
        title="证券（大陆A股）策略回测",
        text="请选择策略",
        values=[
            ("stock_mainland_strategy_check_ene", trader.stock.strategy.Ene.describe),
            (
                "stock_mainland_strategy_check_sma_bs",
                trader.stock.strategy.SmaBS.describe,
            ),
            (
                "stock_mainland_strategy_check_sma_cross",
                trader.stock.strategy.SmaCross.describe,
            ),
        ],
    ).run()

    return result


def show_stock_mainland_strategy_check_ene(session):
    title = trader.stock.strategy.Ene.describe
    symbol = "000002"
    start_date = mainland.params["start_date"]
    end_date = mainland.params["end_date"]
    show_picture = False
    print_log = False

    while True:
        text = input_dialog(title=title, text="请输入6位数字证券代码:").run()
        if text is None:
            return
        else:
            if is_stock_symbol(text):
                symbol = text
                break

    result = checkboxlist_dialog(
        title=title,
        text="是否修改缺省值？",
        values=[
            ("change_start_date", "开始日期，当前值：%s" % start_date),
            ("change_end_date", "结束日期，当前值：%s" % end_date),
            ("change_show_picture", "绘图显示，当前值：否"),
            ("change_print_log", "打印日志，当前值：否"),
        ],
    ).run()

    if result is not None:
        if "change_start_date" in result:
            while True:
                text = input_dialog(title=title, text="请输入开始日期 [格式：20201201]").run()
                if text is None:
                    return
                else:
                    if is_valid_date(text):
                        start_date = text
                        break

        if "change_end_date" in result:
            while True:
                text = input_dialog(title=title, text="请输入结束日期 [格式：20201201]").run()
                if text is None:
                    return
                else:
                    if is_valid_date(text):
                        end_date = text
                        break

        if "change_show_picture" in result:
            show_picture = yes_no_dialog(title=title, text="绘图显示?").run()

        if "change_print_log" in result:
            print_log = yes_no_dialog(title=title, text="打印日志?").run()

    mainland.strategy_check_ene(
        symbol=symbol,
        start_date=start_date,
        end_date=end_date,
        show_picture=show_picture,
        print_log=print_log,
    )


def show_stock_mainland_strategy_check_sma_bs(session):
    title = trader.stock.strategy.SmaBS.describe
    symbol = "000002"
    period = 20
    start_date = mainland.params["start_date"]
    end_date = mainland.params["end_date"]
    show_picture = False
    print_log = False

    while True:
        text = input_dialog(title=title, text="请输入6位数字证券代码:").run()
        if text is None:
            return
        else:
            if is_stock_symbol(text):
                symbol = text
                break

    result = checkboxlist_dialog(
        title=title,
        text="是否修改缺省值？",
        values=[
            ("change_period", "均线周期，当前值：%d" % period),
            ("change_start_date", "开始日期，当前值：%s" % start_date),
            ("change_end_date", "结束日期，当前值：%s" % end_date),
            ("change_show_picture", "绘图显示，当前值：否"),
            ("change_print_log", "打印日志，当前值：否"),
        ],
    ).run()

    if result is not None:
        if "change_period" in result:
            while True:
                text = input_dialog(title=title, text="请输入均线周期 [0-250]:").run()
                if text is None:
                    return
                else:
                    if is_number(text, 0, 60):
                        period = int(text)
                        break

        if "change_start_date" in result:
            while True:
                text = input_dialog(title=title, text="请输入开始日期 [格式：20201201]").run()
                if text is None:
                    return
                else:
                    if is_valid_date(text):
                        start_date = text
                        break

        if "change_end_date" in result:
            while True:
                text = input_dialog(title=title, text="请输入结束日期 [格式：20201201]").run()
                if text is None:
                    return
                else:
                    if is_valid_date(text):
                        end_date = text
                        break

        if "change_show_picture" in result:
            show_picture = yes_no_dialog(title=title, text="绘图显示?").run()

        if "change_print_log" in result:
            print_log = yes_no_dialog(title=title, text="打印日志?").run()

    mainland.strategy_check_sma_bs(
        symbol=symbol,
        period=period,
        start_date=start_date,
        end_date=end_date,
        show_picture=show_picture,
        print_log=print_log,
    )


def show_stock_mainland_strategy_check_sma_cross(session):
    title = trader.stock.strategy.SmaCross.describe
    symbol = "000002"
    pfast = 10
    pslow = 30
    start_date = mainland.params["start_date"]
    end_date = mainland.params["end_date"]
    show_picture = False
    print_log = False

    while True:
        text = input_dialog(title=title, text="请输入6位数字证券代码:").run()
        if text is None:
            return
        else:
            if is_stock_symbol(text):
                symbol = text
                break

    result = checkboxlist_dialog(
        title=title,
        text="是否修改缺省值？",
        values=[
            ("change_pfast", "快速均线周期，当前值：%d" % pfast),
            ("change_pslow", "慢速均线周期，当前值：%d" % pslow),
            ("change_start_date", "开始日期，当前值：%s" % start_date),
            ("change_end_date", "结束日期，当前值：%s" % end_date),
            ("change_show_picture", "绘图显示，当前值：否"),
            ("change_print_log", "打印日志，当前值：否"),
        ],
    ).run()

    if result is not None:
        if "change_pfast" in result:
            while True:
                text = input_dialog(title=title, text="请输入快速均线周期 [0-250]:").run()
                if text is None:
                    return
                else:
                    if is_number(text, 0, 60):
                        pfast = int(text)
                        break

        if "change_pslow" in result:
            while True:
                text = input_dialog(title=title, text="请输入慢速均线周期 [0-250]:").run()
                if text is None:
                    return
                else:
                    if is_number(text, 0, 60):
                        pslow = int(text)
                        break

        if "change_start_date" in result:
            while True:
                text = input_dialog(title=title, text="请输入开始日期 [格式：20201201]").run()
                if text is None:
                    return
                else:
                    if is_valid_date(text):
                        start_date = text
                        break

        if "change_end_date" in result:
            while True:
                text = input_dialog(title=title, text="请输入结束日期 [格式：20201201]").run()
                if text is None:
                    return
                else:
                    if is_valid_date(text):
                        end_date = text
                        break

        if "change_show_picture" in result:
            show_picture = yes_no_dialog(title=title, text="绘图显示?").run()

        if "change_print_log" in result:
            print_log = yes_no_dialog(title=title, text="打印日志?").run()

    mainland.strategy_check_sma_cross(
        symbol=symbol,
        pfast=pfast,
        pslow=pslow,
        start_date=start_date,
        end_date=end_date,
        show_picture=show_picture,
        print_log=print_log,
    )


# This code calls the main function to get everything started.
# The condition is True when the module is executed by the interpreter,
# but False when it is imported into another module.
if __name__ == "__main__":
    main()
