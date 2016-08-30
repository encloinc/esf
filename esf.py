#       ______ _____  ______
#      / ____// ___/ / ____/
#     / __/   \__ \ / /_
#    / /___  ___/ // __/
#   /_____/ /____//_/
#                       The easiest way to save arrays on a file, saved on a .ESF format (;
import os
import engine

class EasySaveFunctions:
    def __init__(self, filepath, name):
        self.file_path_ = filepath
        self.name_ = name
        self.directory_ = os.path.join(self.file_path_, self.name_)
        if not os.path.exists(self.file_path_):
            os.makedirs(self.file_path_)
        try:
            f = open(self.directory_, 'r')
            string = f.read()
            f.close()
        except FileNotFoundError:
            f = open(self.directory_, 'w')
            f.close()

    def append(self, payload):
        if check_format(self.directory_) == 'True':
            if not os.path.exists(self.directory_):
                f = open(self.directory_, 'w')
                f.close()
            else:
                f = open(self.directory_, 'r')
                string = f.read()
                tmp = engine.decode(string)
                f.close()
                f = open(self.directory_, 'w')
                tmp.append(payload)
                f.write(engine.encode(tmp))
                f.close()

    def replace(self, item, payload):
        if check_format(self.directory_) == 'True':
            if not os.path.exists(self.directory_):
                os.makedirs(self.directory_)
                f = open(self.directory_, 'w')
                f.close()
            else:
                f = open(self.directory_, 'r')
                string = f.read()
                f.close()
                f = open(self.directory_, 'w')
                tmp = engine.decode(string)
                tmp.pop(item)
                tmp.insert(item, payload)
                f.write(engine.encode(tmp))
                f.close()

    def pop(self, item):
        if check_format(self.directory_) == 'True':
            if not os.path.exists(self.directory_):
                os.makedirs(self.directory_)
                f = open(self.directory_, 'w')
                f.close()
            else:
                f = open(self.directory_, 'r')
                string = f.read()
                tmp = engine.decode(string)
                tmp.pop(item)
                f.close()
                f = open(self.directory_, 'w')
                f.write(engine.encode(tmp))
                f.close()
    def index(self, index):
        if check_format(self.directory_) == 'True':
            if not os.path.exists(self.directory_):
                os.makedirs(self.directory_)
                f = open(self.directory_, 'w')
                f.close()
            else:
                f = open(self.directory_, 'r')
                string = f.read()
                tmp = engine.decode(string)
                return tmp.index(index)
    def delete(self):
        if check_format(self.directory_) == 'True':
            if not os.path.exists(self.directory_):
                os.makedirs(self.directory_)
                f = open(self.directory_, 'w')
                f.close()
            else:
                os.remove(self.directory_)
    def get_list(self):
        if check_format(self.directory_) == 'True':
            if not os.path.exists(self.directory_):
                os.makedirs(self.directory_)
                f = open(self.directory_, 'w')
                f.close()
            else:
                f = open(self.directory_, "r")
                string = f.read()
                return engine.decode(string)
                f.close()
    def upload_list(self, list):
        if check_format(self.directory_) == 'True':
            if not os.path.exists(self.directory_):
                os.makedirs(self.directory_)
                f = open(self.directory_, 'w')
                f.close()
            else:
                f = open(self.directory_, 'w')
                f.write(engine.encode(list))
                f.close()


def check_format(x):
    e = x[len(x) - 3] + x[len(x) - 2] + x[len(x) - 1]
    if e == 'esf':
        return('True')
    else:
        return('False')
        print('Not ESF FILE!')
