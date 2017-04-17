import os
import re
import Srm_Parse


class RemoveHandler:

    class Singleton():
        def __init__(self):
            RemoveHandler.path_to_trash = './trash'

    instance = None

    path_to_trash = None

    list_to_remove = []

    def __init__(self):
        if not RemoveHandler.instance:
            RemoveHandler.instance = RemoveHandler.Singleton()

    def remove_regexp(self, paths, regexp):
        for path in list(paths):
            if str(path) == self.path_to_trash:
                pass
            if os.path.isdir(path):
                for name in os.listdir(path):
                    if re.match(regexp, name):
                        self.remove(os.path.join(path, name))
                    else:
                        if os.path.isdir(os.path.join(path, name)):
                            self.delete_regexp(os.path.join(path, name), regexp)
                    self.remove(path)
            else:
                self.remove(path)

    def remove(self, paths):
        for path in list(paths):
            if not self.path_to_trash.find(str(path)):
                self.list_to_remove.append(path)


def main():

    srm = RemoveHandler()
    srm.remove_regexp(Srm_Parse.list_remove_regex, Srm_Parse.args.regexp_r[0])
    srm.remove(Srm_Parse.list_remove)

if __name__ == '__main__':
    main()