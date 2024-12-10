from datetime import datetime

"""
%Y: 4-digit year (e.g., 2024)
%y: 2-digit year (e.g., 24)
%m: 2-digit month (01-12)
%B: Full month name (e.g., December)
%b: Abbreviated month name (e.g., Dec)
%d: 2-digit day of the month (01-31)
%A: Full weekday name (e.g., Sunday)
%a: Abbreviated weekday name (e.g., Sun)
%H: 24-hour clock hour (00-23)
%I: 12-hour clock hour (01-12)
%M: Minutes (00-59)
%S: Seconds (00-59)
%p: AM/PM
%z: UTC offset (e.g., +0800)
"""


def get_time() -> str:
    now: datetime = datetime.now()
    return f"{now:%I:%M%p}"


print(get_time())
