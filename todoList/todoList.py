import re

print('Hello TodoList Program~')
name = input("请输入用户名：").strip()


# 解析日期 或者 时间
def analyse(str_input: str, mode: str):
    if mode == 'date':
        regexp = "\d{4}-\d{2}-\d{2}"
    if mode == 'time':
        regexp = "\d{2}:\d{2}"
    search_result = re.search(regexp, str_input)
    if search_result:
        return search_result.group(0)
    else:
        return None


def read_file(filename: str):
    try:
        file = open(filename + '.sav', 'r')
        file_content = file.read()
        todo_lines = file_content.splitlines()
        saved_todos = []
        for todo_in_line in todo_lines:
            # 对读取到的每一行进行解析，获取日期、时间、内容
            specified_todo = {
                'date': analyse(todo_in_line, 'date'),
                'time': analyse(todo_in_line, 'time'),
                'detail': todo_in_line
            }
            saved_todos.append(specified_todo)
        return saved_todos
    except IOError:
        return []


def handle_user_options():
    pass


def handle_user_input(user_input: str):
    user_input = user_input.strip()
    if user_input == 'OP':
        handle_user_options()
    else:
        date = analyse(user_input, 'date')



try:
    f = open(name + '.sav', 'r')

    fileContent = f.read()
    todos = fileContent.splitlines()
    print(todos)
    while 1:
        i = input("请输入待办事项：").strip()
        # eg:
        # 2021-06-06 20:00 看书
        if i == 'OP':
            # 输入OP后，进入功能选择
            print('请输入要选择的功能: PRINT/number/SEARCH/RESET/END/SAVE/QUIT')
            op = input()
            if op == 'PRINT':
                # 输入PRINT，打印所有输入的待完成事项（包括事项和截止时间）
                for todo in todos:
                    print(todo)
            elif isinstance(op, int):
                # 输入数字，则打印待完成事项的第几项，如果事项数不够，提示错误（修改为异常处理模式）
                pass
            elif op == 'SEARCH':
                # 输入SEARCH，则等待用户输入一个正则表达式，可以根据输入的正则表达式打印出所有匹配的待办事项
                pass
            elif op == 'RESET':
                # 输入RESET，删除所有信息；
                pass
            elif op == 'SAVE':
                # 输入SAVE，等待用户输入目标文件，然后将用户数据保存至用户指定的文件中（另存为）
                newNameStr = input()
                newFile = open(newNameStr, 'w')
                newFile.write(todos)
                newFile.close()
                pass
            elif op == 'QUIT':
                # 输入QUIT，保存数据至用户的存档文件，终止程序
                f.flush()
                f.close()
                break
            else:
                print('未知指令，请重新输入')
            pass
        else:
            pass
except IOError as e:
    print(e)
