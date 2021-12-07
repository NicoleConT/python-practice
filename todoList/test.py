import re


# 解析日期 或者 时间
def analyse(str_input, mode):
    if mode == 'date':
        regexp = "\d{4}-\d{2}-\d{2}"
    if mode == 'time':
        regexp = "\d{2}:\d{2}"
    search_result = re.search(regexp, str_input)
    if search_result:
        return search_result.group(0)
    else:
        return None


str_input = input('input a string for match\n').strip()
mode = input('input search mode(date/time):\n').strip()
result = analyse(str_input, mode)
print(result)
