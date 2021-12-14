import os
from functools import reduce


class File:

    def __init__(self, file_path, file_name):
        self.__file_name = file_name
        with open(os.path.join(file_path, file_name), "r", encoding="UTF-8") as file:
            self.__lines = file.readlines()
            self.__lines_count = len(self.__lines)

    def get_file_name(self):
        return self.__file_name

    def get_lines(self):
        return self.__lines

    def get_lines_count(self):
        return self.__lines_count

    def get_data(self):
        return [self.__file_name, str(self.__lines_count)] + self.__lines

    def __lt__(self, other):
        return self.__lines_count < other.__lines_count


class Folder:

    def __init__(self, path="./files"):
        self.__path = path
        self.__files = []

    def read(self):
        self.__files = [File(self.__path, file_name) for file_name in os.listdir(self.__path)
                        if (".txt" == os.path.splitext(file_name)[1])
                        and ("total.txt" != file_name)
                        and os.path.isfile(os.path.join(self.__path, file_name))]

    def print(self):
        print(list(f.get_file_name() for f in self.__files))

    def get_data(self):
        return reduce(lambda l, r: l + r, map(File.get_data, sorted(self.__files)))

    def write_total_file(self):
        with open(os.path.join(self.__path, "total.txt"), "w", encoding="UTF-8") as file:
            for line in self.get_data():
                print(line.strip(), file=file)


folder = Folder()
folder.read()
folder.print()

print(folder.get_data())

folder.write_total_file()
