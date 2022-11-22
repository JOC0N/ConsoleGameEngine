import CFH

# CGE - Central Game Engine


# ----------

CGE_version = str("1.2").strip()
creator = str("JOC0N")
CFH_txt_save = str("save.txt")
CFH_json_lang = str("lang/en.json")
save_list = []


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


def menu_choice_create(options: list):
    choice_amount = int(len(options))
    for index, option in enumerate(options):
        print(CFH.json_read(CFH_json_lang, ["appearance", "choice_char_l"]),
              index + 1,
              CFH.json_read(CFH_json_lang, ["appearance", "choice_char_r"]),
              str(option)
              )
    return choice_amount


def menu_title():
    output(CFH.json_read(CFH_json_lang, ["main", "title"]))
    return True


def menu_options(question: str, options: list):
    print(question)
    temp = menu_choice_create(options)
    return menu_filter(temp)


def menu_yon(question: str):
    print(question)
    options = [
        CFH.json_read(CFH_json_lang, ["appearance", "choice_yes"]),
        CFH.json_read(CFH_json_lang, ["appearance", "choice_no"])
        ]
    temp = menu_choice_create(options)
    return menu_filter(temp)


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
    output(CFH.json_read(CFH_json_lang, ["save", "save_new"]))
    CFH.file_create(CFH_txt_save)
    CFH.file_write(CFH_txt_save, f"{CFH.json_read(CFH_json_lang, ['main', 'title'])} --- by {creator} --- Version: ")
    CFH.file_write(CFH_txt_save, CGE_version)
    for line in CFH.file_load_list(CFH_txt_save):
        save_list.append(line)
    return True


def load_save():
    save_version = CFH.file_read(CFH_txt_save, 2).strip()

    if not CFH.file_exists(CFH_txt_save):
        output_list([CFH.json_read(CFH_json_lang, ['Error_save', 'not_exists_1']),
                     CFH.json_read(CFH_json_lang, ['Error_save', 'not_exists_2'])
                     ])
        return False
    elif CFH.file_empty(CFH_txt_save):
        output(CFH_txt_save + CFH.json_read(CFH_json_lang, ['Error_save', 'is_empty']))
        return False
    elif CFH.file_line_count(CFH_txt_save) < 2:
        output(CFH_txt_save + CFH.json_read(CFH_json_lang, ['Error_save', 'file_corrupted']))
        return False
    elif CGE_version != save_version:
        output_list([CFH_txt_save + CFH.json_read(CFH_json_lang, ['Error_save', 'CGE_version']),
                     "CGE: " + CGE_version, CFH_txt_save + ": " + save_version])
        return False
    else:
        output(CFH.json_read(CFH_json_lang, ['save', 'save_restore']))
        for line in CFH.file_load_list(CFH_txt_save):
            save_list.append(line)
        return True


def save():
    answer = menu_yon(CFH.json_read(CFH_json_lang, ['save', 'save_question']))
    if answer == 1:
        output(CFH.json_read(CFH_json_lang, ['save', 'save_accept']))
        CFH.file_save_list(CFH_txt_save, save_list)
        return True
    if answer == 2:
        output(CFH.json_read(CFH_json_lang, ['save', 'save_deny']))
        return False
