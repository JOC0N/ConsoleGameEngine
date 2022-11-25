import random

import CGE


def start_menu():
    status = False
    CGE.menu_title()

    while not status:
        answer = CGE.menu_yon(CGE.lang("save", "new_game"))
        if answer == 1:
            status = CGE.new_save()
        elif answer == 2:
            status = CGE.load_save()


def game():
    answer = CGE.menu_options(CGE.lang("ex_1", "qu_1"),
                              [CGE.lang("ex_1", "op_1"),
                               CGE.lang("ex_1", "op_2"),
                               CGE.lang("ex_1", "op_3")])
    if answer == 1:
        CGE.output(CGE.lang("ex_1", "out_1"))
        CGE.save()
    elif answer == 2:
        CGE.save()
    elif answer == 3:
        CGE.output(CGE.lang("ex_1", "out_2"))
        CGE.save()


if __name__ == '__main__':
    start_menu()
    game()
