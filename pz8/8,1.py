import os
import linecache

file_base = "base.txt"
all_data = []

if not os.path.exists(file_base):
    with open(file_base, "w", encoding="utf-8") as _:
        pass


def read_records():
    global all_data, file_base
    with open(file_base) as f:
        all_data = [i.strip() for i in f]
        return all_data


def add_new_contact():
    f = open('base.txt', 'rb')
    id = len(f.readlines()) + 1
    array = ['sutname', 'name', 'surname2', 'phone number']
    string = ''
    for i in array:
        string = string + input(f'enter + {i}: ') + ' '
    with open(file_base, "a", encoding="utf-8") as f:
        f.write(f"{id} {string}\n")


def show_all():
    with open('base.txt', "r", encoding="utf-8") as file1:
        file1.seek(0)
        first_char = file1.read(1)
        if not first_char:
            print("file is empty")
        else:
            print(file1.read())


def search(word):
    inp = open('base.txt').readlines()
    for i in iter(inp):
        if word in i:
            print(i)


def renumerate():
    with open('temp.txt', 'r') as read_object, open('base.txt', 'w') as write_object:
        for idx, line in enumerate(read_object, start=1):
            write_object.write('{} {}'. format(idx, line))


def delete_previous():
    f = open("base.txt", "r+")
    lines = f.readlines()
    f.seek(0)
    for line in lines:
        line = line[1:]
        f.write(line)
    f.truncate()


def searchid(line_no):
    print(linecache.getline('base.txt', line_no))


def delete_by_data(word):
    delete_previous()

    with open("base.txt", "r") as input:
        with open("temp.txt", "w") as output:
            for line in input:
                if word not in line.strip("\n"):
                    output.write(line)

    renumerate()


def delete_by_id(chislo):
    delete_previous()

    with open("base.txt", 'r') as fp:
        lines = fp.readlines()
    with open("temp.txt", 'w') as output:
        for number, line in enumerate(lines, start=1):
            if number != chislo:
                output.write(line)

    renumerate()


def main_menu():
    play = True
    while play:
        read_records()
        answer = input("Phone book:\n"
                       "1. Show all records\n"
                       "2. Add a record\n"
                       "3. Search a record\n"
                       "4. Delete\n"
                       "5. Exit\n")
        match answer:
            case "1":
                show_all()
            case "2":
                add_new_contact()
            case "3":
                answer = input("Records:\n"
                               "1. ID\n"
                               "2. Data\n")
                match answer:
                    case "1":
                        searchid(int(input()))
                    case "2":
                        search(input())
            case "4":
                answer = input("DELETE:\n"
                               "1. ID\n"
                               "2. DATA\n")
                match answer:
                    case "1":
                        delete_by_id(int(input()))
                    case "2":
                        delete_by_data(input())

            case "5":
                play = False
            case _:
                print("Try again!\n")


main_menu()
