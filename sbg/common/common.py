from datetime import datetime


def driver_path():
    return r"C:\Users\xua\Downloads\chromedriver_win32\chromedriver.exe"


def base_url():
    return "https://www.smartbuyglasses.com"


def get_current_time():
    format_time = "%a %b %d %H:%M:%S %Y"
    return datetime.now().strftime(format_time)


def time_different(start_time, end_time):
    format_time = "%a %b %d %H:%M:%S %Y"
    return datetime.strptime(end_time, format_time) - datetime.strptime(start_time, format_time)


