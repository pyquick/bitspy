def checkdate(dates:list):
    for i in dates:
        if not isinstance(i, str):
            return False
        try:
            date= i.split('-')
            if len(date) != 3:
                return False
            year, month, day = map(int, date)
            year = int(year)
            month = int(month)
            day = int(day)
            if year < 0:
               return False
            if not (1 <= month <= 12):
                return False
            if not (1 <= day <= 31):
                return False
            if year % 4!=0 and month == 2 and day > 28:
                return False
            if year %4==0 and year%400!=0 and month == 2 and day > 28:
               return False
            if month in [4, 6, 9, 11] and day > 30:
                return False
            if month == 2 and day > 29:
                return False
        except ValueError as e:
            return False
        return True
def check_a_date(date:str):
    if not isinstance(date, str):
        return False
    try:
        year, month, day = map(int, date.split('-'))
        if year < 0:
            return False
        if not (1 <= month <= 12):
            return False
        if not (1 <= day <= 31):
            return False
        if year % 4 != 0 and month == 2 and day > 28:
            return False
        if year % 4 == 0 and year % 100 != 0 and month == 2 and day > 28:
            return False
        if month in [4, 6, 9, 11] and day > 30:
            return False
        if month == 2 and day > 29:
            return False
    except ValueError as e:
        return False
    return True
def split_a_date(date:str) -> tuple:
    if not check_a_date(date):
        raise ValueError("Invalid date format. Expected format: YYYY-MM-DD")
    year, month, day = date.split('-')
    return int(year), int(month), int(day)
def spiltdates(dates:str)->list[tuple]:
    if not checkdate(dates):
        raise ValueError("Invalid date format in the list. Expected format: YYYY-MM-DD")
    return [split_a_date(date) for date in dates]
