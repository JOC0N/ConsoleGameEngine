import json
import os


# CFH - Central File Handler


# TXT Files----------

def file_exists(filepath: str):
    if os.path.exists(filepath) and os.path.isfile(filepath):
        return True


def file_empty(filepath: str):
    if os.path.getsize(filepath) == 0:
        return True


def file_line_count(filepath: str):
    with open(filepath, 'r') as file:
        for line_amount, lines in enumerate(file):
            pass
    return line_amount + 1


def file_create(filepath: str):
    with open(filepath, "w") as file:
        file.close()
    return True


def file_write(filepath: str, text: str):
    with open(filepath, "a") as file:
        file.write(str(text) + "\n")
    return True


def file_read(filepath: str, line_number: int):
    with open(filepath, "r") as file:
        lines = file.readlines()
        return lines[line_number - 1]


def file_load_list(filepath: str):
    with open(filepath, 'r') as file:
        file2list = file.read().splitlines()
    return file2list


def file_save_list(filepath: str, list2file: list):
    file_create(filepath)
    for line in list2file:
        file_write(filepath, line)
    return True


# JSON Files----------

def json_read(filepath: str, value_path: list):
    with open(filepath, "r") as file:
        data = json.load(file)

        return data[value_path[0]][value_path[1]]
