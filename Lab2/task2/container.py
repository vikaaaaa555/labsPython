import re
import json


class UniqueContainer:
    def __int__(self, username):
        self.username = username
        self.data = {}


    def add(self, *args):
        if self.username not in self.data:
            self.data[self.username] = list(args)
        else:
            for element in args:
                if element not in self.data[self.username]:
                    self.data[self.username].append(element)


    def remove(self, key):
        self.elements.discard(key)