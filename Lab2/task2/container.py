import re
import json


class UniqueContainer:
    def __init__(self, username):
        self.username = username
        self.data = dict()
        self.loaded = False


    def add(self, *args):
        if self.username not in self.data:
            self.data[self.username] = list(args)
        else:
            for element in args:
                if element not in self.data[self.username]:
                    self.data[self.username].append(element)


    def remove(self, arg):
        if self.username not in self.data or not self.data[self.username]:
            print("The container is empty")
        elif arg not in self.data[self.username]:
            print("These elements are not in the container")
        else:
            self.data[self.username].remove(arg)


    def find(self, *args):
        if self.username not in self.data or not self.data[self.username]:
            print("The container is empty")

        find_args = [arg for arg in args if arg in self.data[self.username]]
        if find_args == 0:
            print("These elements are not in the container" )
        else:
            print("Found elements: ", *find_args)


    def list(self):
        if self.username not in self.data or not self.data[self.username]:
            print("The container is empty")
        else:
            print(self.data[self.username])


    def grep(self, regex: re):
        if self.username not in self.data or not self.data[self.username]:
            print("The container is empty")

        found_reg = []
        for element in self.data[self.username]:
            if re.search(regex, element):
                found_reg.append(element)
        if found_reg:
            print(", ".join(found_reg))


    def load(self):
        self.loaded = True
        temp = self.data
        with open("data.json", "r") as f:
            self.data = json.load(f)

        if self.username in self.data and self.username in temp:
            if temp[self.username] != self.data[self.username]:
                self.add(*temp[self.username])


    def save(self):
        if not self.loaded:
            temp_data = self.data
            with open('data.json', 'r') as file:
                self.data = json.load(file)
            if self.username in temp_data and self.username in self.data:
                if temp_data[self.username] != self.data[self.username]:
                    self.add(*temp_data[self.username])

        if self.username not in self.data or not self.data[self.username]:
            self.data[self.username] = []
        with open("data.json", "w") as f:
            json.dump(self.data, f)


    def load_username(self):
        with open("data.json", "r") as f:
            self.data = json.load(f)

        if self.username in self.data:
            self.data[self.username] = []


    def switch(self, username):
        self.username = username
        self.data = {}
