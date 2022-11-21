import CFH

# CGE - Central Game Engine

version = str(1.1)
CFH_file = str("save.txt")
save = []

# ----------


def menu_filter(amount: int):
    menu_answer = -1
    while menu_answer <= 0 or menu_answer > amount:
        try:
            menu_answer = int(input())
        except (ValueError, RuntimeError, TypeError, NameError):
            menu_answer = -1
    print()
    return menu_answer


def menu_options(question: str, options: list):
    amount = int(len(options))
    print(question)
    for index, option in enumerate(options):
        print("[", index + 1, "] ", str(option))
    return menu_filter(amount)


def menu_yon(question: str):
    amount = 2
    print(question)
    print("[1] Yes")
    print("[2] No")
    return menu_filter(amount)


def menu_text(question: str):
    print(question)
    menu_answer = input()
    print()
    return str(menu_answer)


def output(text: str):
    print(text)
    print()


def output_list(text: list):
    for line in text:
        print(str(line))
    print()


def new_save():
    output("Starting new game...")
    CFH.file_create(CFH_file)
    CFH.file_write(CFH_file, "-----Text Adventure-----by JOC0N-----Version:")
    CFH.file_write(CFH_file, version)
    return True


def resume_save():
    if not CFH.file_exists(CFH_file):
        output_list(["Save does not exist!", "Please make sure its in the same directory!"])
        return False
    elif CFH.file_empty(CFH_file):
        output(CFH_file + " is empty!")
        return False
    elif CFH.file_line_count(CFH_file) < 2:
        output(CFH_file + " is corrupted or not complete!")
        return False
    elif version == CFH.file_read(CFH_file, 2):
        output_list([CFH_file + " is not valid!", "Please make sure its the same game version "])
        output_list(["Current version: " + version, "Savefile version: " + version])
        return False
    else:
        output("Resuming game...")
        for line in CFH.file_load_list(CFH_file):
            save.append(line)
        print(save)
        return True
