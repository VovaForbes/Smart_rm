import os
import datetime as dt
import shutil
import SrmF98
import Trash_Parse


class Trash:

    class Singleton:
        def __init__(self):
            print "Trash was successfully installed!"
            os.mkdir(Trash.path_to_trash)
            os.mkdir(Trash.info)
            os.mkdir(Trash.files)

    def __init__(self):
        if not Trash.instance:
            Trash.instance = Trash.Singleton()

    instance = None

    path_to_trash = './trash'
    info = path_to_trash + '/info'
    files = path_to_trash + '/files'

    def add_to_trash(self, paths):
        for path in paths:
            copy_number = -1
            name_already_exists = True
            while name_already_exists:
                copy_number += 1
                str_copy_number = '(' + str(copy_number) + ')'
                if copy_number > 0:
                    name_already_exists = self.path_is_correct(os.path.join(self.info, os.path.basename(path)
                                                                            + str_copy_number))
                else:
                    name_already_exists = self.path_is_correct(os.path.join(self.info, os.path.basename(path)))

            if copy_number > 0:
                os.rename(path, os.path.join(self.files, os.path.basename(path) + str_copy_number))
            else:
                os.rename(path, os.path.join(self.files, os.path.basename(path)))

            if copy_number > 0:
                with open(os.path.join(self.info, os.path.basename(path) + str_copy_number), 'w') as file_:
                    file_.write(path + '\n' + str(dt.datetime.now()))
            else:
                with open(os.path.join(self.info, os.path.basename(path)), 'w') as file_:
                    file_.write(path + '\n' + str(dt.datetime.now()))

    def restore(self, names):
        for name in list(names):
            with open(os.path.join(self.info, name), 'r') as file_:
                rest_path = file_.readline()[:-1]
                os.rename(os.path.join(self.files, name), rest_path)
                os.remove(os.path.join(self.info, name))

    def clear_trash(self):
        for filename in os.listdir(self.files):
            shutil.rmtree(filename)

    def list(self, amount):
        count = 0
        for filename in os.listdir(self.files):
            count += 1
            print "\n{0}). {1} ----- {2}bytes".format(str(count), filename,
                                                      os.path.getsize(os.path.join(self.files, filename)))
            if count == amount:
                return


def main():

    trash = Trash()
    trash.add_to_trash(SrmF98.Remove_Handler.list_to_remove)
    trash.restore(Trash_Parse.list_to_restore)
    if Trash_Parse.clear_:
        trash.clear_trash()
    trash.list(Trash_Parse.list_)

if __name__ == '__main__':
    main()


