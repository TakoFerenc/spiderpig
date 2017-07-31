import os
import datetime


class FileHandler:

        def __init__(self, filename=None):
            self.filename = filename

        def write_to_file(self, line_iterator):
            with open(self.filename, 'a') as fa:
                for line in line_iterator:
                    fa.write(str(line) + '\n')

        def read_from_file(self):
            with open(self.filename, 'r') as fr:
                lines = fr.readlines()
                for line in lines:
                    yield line

        def rename_file(self):
            dest = 'C:\\Users\\Fred\\PycharmProjects\\spiderpig\\'
            date = str(datetime.datetime.today()).replace(':', '_').replace(' ', '_')
            new_name = f'result_{date}.txt'
            if not (os.path.isfile(dest + new_name)):
                os.rename(self.filename, new_name)

        def create_file_temp(self):
            dest = 'C:\\Users\\Fred\\PycharmProjects\\spiderpig\\'
            name = f'result_temp.txt'
            if not (os.path.isfile(dest + name)):
                with open(dest + name, 'w') as fw:
                    fw.write('\n')
            self.filename = name
            return self.filename
