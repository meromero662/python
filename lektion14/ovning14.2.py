
import ui



def line(dots=False):
    if dots:
        print('*' * 30)
    else:
        print('-' * 30)

def header(text):
    padding = (30 - len(text)) // 2
    left_padding = padding
    right_padding = 30 - len(text) - left_padding
    header_text = '|' + ' ' * left_padding + text + ' ' * right_padding + '|'
    line()
    print(header_text)
    line()

def echo(text):
    left_padding = 2
    echo_text = '|' + ' ' * left_padding + text
    print(echo_text)

def prompt(text):
    left_padding = 2
    prompt_text = '|' + ' ' * left_padding + text + ' > '
    user_input = input(prompt_text)
    return user_input

def clear():
    print('\033c')  # Clear the terminal screen










