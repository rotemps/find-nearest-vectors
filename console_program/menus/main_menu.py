import enum

from console_program.menus.add_menu import open_add_menu
from console_program.menus.query_menu import open_query_menu


class Option(enum.Enum):
    ADD = 'add'
    QUERY = 'query'
    QUIT = 'quit'

    @classmethod
    def has_value(cls, value):
        return value in cls._value2member_map_


def open_main_menu(kd_tree):
    print_menu_instructions()

    while True:
        user_input = get_user_input()
        if not Option.has_value(user_input):
            print("Invalid Option!")
            continue

        if user_input == Option.QUIT.value:
            break

        if user_input == Option.ADD.value:
            open_add_menu(kd_tree)
        elif user_input == Option.QUERY.value:
            open_query_menu(kd_tree)

        print_menu_instructions()


def get_user_input():
    return input("")


def print_menu_instructions():
    print(
        '===============\n'
        'Please select one of the following options:\n'
        f'{Option.ADD.value} - add vectors\n'
        f'{Option.QUERY.value} - query vectors\n'
        f'{Option.QUIT.value} - quit program\n'
        '===============\n'
    )
