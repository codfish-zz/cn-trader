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

from datetime import datetime, date, timedelta


# 返回距当前时间 days 天之前的时间
def get_date_before(days):
    today = date.today()
    return today - timedelta(days=days)


# 返回距当前时间 days 天之后的时间
def get_date_after(days):
    today = date.today()
    return today + timedelta(days=days)


def is_number(text, min, max):
    result = False

    if text is not None:
        if text.isdigit():
            value = int(text)
            if value >= min and value <= max:
                result = True

    return result


def is_stock_symbol(text):
    result = False

    if text is not None:
        if text.isdigit() and len(text) == 6:
            if text.startswith("0") or text.startswith("3") or text.startswith("6"):
                result = True

    return result


def is_valid_date(date):
    if date is None:
        return False
    if not date.isdigit():
        return False
    if len(date) != 8:
        return False

    try:
        datetime.strptime(date, "%Y%m%d")
        return True
    except:
        return False
