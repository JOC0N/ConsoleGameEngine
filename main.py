import CGE


def main():
    status = False
    CGE.output("Text Adventure")
    while status is False:
        answer = CGE.menu_yon("Start a new game?")
        if answer == 1:
            status = CGE.new_save()
        if answer == 2:
            status = CGE.resume_save()


if __name__ == '__main__':
    main()






