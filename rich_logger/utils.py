import re
from time import gmtime, strftime


def get_date_as_regex(time_format: str):
    if time_format.find("%") >= 0:
        time_format_copy = strftime(time_format, gmtime())
    else:
        time_format_copy = time_format
    regex_time = ""

    while len(time_format_copy) > 0:
        search_non_digit = re.search(r"\D", time_format_copy)
        if search_non_digit is not None:
            non_digit_index = re.search(r"\D", time_format_copy).start()
            regex_time += r"\d{" + str(non_digit_index) + r"}" + time_format_copy[non_digit_index]
        else:
            non_digit_index = len(time_format_copy)
            regex_time += r"\d{" + str(non_digit_index) + r"}"
        time_format_copy = time_format_copy[non_digit_index + 1 :]
    return regex_time
