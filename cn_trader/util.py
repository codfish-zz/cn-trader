from datetime import datetime


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
