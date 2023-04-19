import re
import json


class UniqueContainer:
    def __int__(self, username):
        self.username = username
        self.data = {}
        self.loaded = False


    def add(self, *args):
        if self.username not in self.data:
            self.data[self.username] = list(args)
        else:
            for element in args:
                if element not in self.data[self.username]:
                    self.data[self.username].append(element)


    def remove(self, arg):
        self.username.discard(arg)
        if self.username not in self.data:
            print("Container is empty")
        elif arg not in self.data:
            print("These elements are not in the container")
        else:
            self.data[self.username].remove(arg)


    def find(self, *args):