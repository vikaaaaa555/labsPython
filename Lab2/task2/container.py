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
            print("The container is empty")
        elif arg not in self.data:
            print("These elements are not in the container")
        else:
            self.data[self.username].remove(arg)


    def find(self, *args):
        if self.username not in self.data:
            print("The container is empty")

        find_args = [arg for arg in args if arg in self.data[self.username]]
        if find_args == 0:
            print("These elements are not in the container" )
        else:
            print("Found elements: ", *find_args)


    def list(self):
        if self.username not in self.data:
            print("The container is empty")
        else:
            print(self.data[self.username])


    def grep(self, regex: re):
        if self.username not in self.data:
            print("The container is empty")

        found_reg = []
        for element in self.data[self.username]:
            if re.search(regex, element):
                found_reg.append(element)
        if found_reg:
            print(", ".join(found_reg))


