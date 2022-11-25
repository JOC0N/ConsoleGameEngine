import CFH

# CGE - Central Game Engine


# ----------

CGE_version = str("1.3").strip()
creator = str("JOC0N")
CFH_txt_save = str("save.txt")
CFH_json_lang = str("lang/en.json")
save_list = []


# ----------

# Makes the handling with languages easier to code
def lang(group: str, value: str):
    return CFH.json_read(CFH_json_lang, [group, value])


# Limits the choice of player to the amount of options
def menu_filter(amount: int):
    answer = -1
    while answer <= 0 or answer > amount:
        try:
            answer = int(input())
        except (ValueError, RuntimeError, TypeError, NameError):
            answer = -1
    print()
    return answer


# Output all options for a question 
def menu_choice_create(options: list):
    amount = int(len(options))
    for index, option in enumerate(options):
        print(lang("appearance", "choice_char_l"), index + 1, lang("appearance", "choice_char_r"), str(option))
    return amount


# Menu with question - Given answers - Input: int() 
def menu_options(question: str, options: list):
    print(question)
    return menu_filter(menu_choice_create(options))


# Menu with question - Yes or No answer - Input: int(1-2)
def menu_yon(question: str):
    print(question)
    options = [lang("appearance", "choice_yes"), lang("appearance", "choice_no")]
    return menu_filter(menu_choice_create(options))


# Menu with question - Text - Input: str()
def menu_text(question: str):
    print(question)
    answer = input()
    print()
    return str(answer)


# Like output()  just fixed to title
def menu_title():
    output(lang("main", "title"))
    return True


# Output a single line
def output(text: str):
    print(text)
    print()


# Output multiple lines without spacing
def output_list(text: list):
    for line in text:
        print(str(line))
    print()


# Clear old save file and create a new one.
def new_save():
    output(lang("save", "save_new"))
    CFH.file_create(CFH_txt_save)
    CFH.file_write(CFH_txt_save, f"{lang('main', 'title')} --- by {creator} --- Version: ")
    CFH.file_write(CFH_txt_save, CGE_version)
    for line in CFH.file_load_list(CFH_txt_save):
        save_list.append(line)
    return True


# Load the save file and checks if it's okay.
def load_save():
    save_version = CFH.file_read(CFH_txt_save, 2).strip()

    if not CFH.file_exists(CFH_txt_save):
        output_list([lang('error_save', 'not_exists_1'), lang('error_save', 'not_exists_2')])
        return False
    elif CFH.file_empty(CFH_txt_save):
        output(CFH_txt_save + lang('error_save', 'is_empty'))
        return False
    elif CFH.file_line_count(CFH_txt_save) < 2:
        output(CFH_txt_save + lang('error_save', 'file_corrupted'))
        return False
    elif CGE_version != save_version:
        output_list([CFH_txt_save + lang('error_save', 'CGE_version'),
                     "CGE: " + CGE_version, CFH_txt_save + ": " + save_version])
        return False
    else:
        output(lang('save', 'save_restore'))
        for line in CFH.file_load_list(CFH_txt_save):
            save_list.append(line)
        return True


# Save the game without asking the player.
def background_save():
    CFH.file_save_list(CFH_txt_save, save_list)
    return True


# Save the game by asking the player to.
def save():
    answer = menu_yon(lang('save', 'save_question'))
    if answer == 1:
        output(lang('save', 'save_accept'))
        background_save()
        return True
    if answer == 2:
        output(lang('save', 'save_deny'))
        return False
