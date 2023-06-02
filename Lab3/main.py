from argparse import ArgumentParser
from py_serializer.serializer import Serializer

if __name__ == '__main__':
    parser = ArgumentParser(description="Serializer JSON, XML")

    parser.add_argument("file_from", type=str, help="file from which you load data")
    parser.add_argument("file_to", type=str, help="file to which you save serialized data")
    parser.add_argument("format_from", type=str, help="format from which you deserialize data (json/xml)")
    parser.add_argument("format_to", type=str, help="format to which you serialize data (json/xml)")

    try:
        args = parser.parse_args()
        file_from = args.file_from
        file_to = args.file_to
        format_from = args.format_from
        format_to = args.format_to
    except SystemExit:
        file_from = "files/json_format.json"
        file_to = "files/xml_format.xml"
        format_from = "json"
        format_to = "xml"

    from_serializer = Serializer.create_serializer(format_from)
    to_serializer = Serializer.create_serializer(format_to)

    obj = from_serializer.load(file_from)
    print(f'Result = {obj}')
    to_serializer.dump(obj, file_to)

import math
from py_serializer.serializer import Serializer


def my_decor(meth):
    def inner(*args, **kwargs):
        print('I am in my_decor')
        return meth(*args, **kwargs)

    return inner


class A:
    x = 10

    @my_decor
    def my_sin(self, c):
        return math.sin(c * self.x)

    @staticmethod
    def stat():
        return 145

    def __str__(self):
        return 'AAAAA'

    def __repr__(self):
        return 'AAAAA'


class B:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    @property
    def prop(self):
        return self.a * self.b

    @classmethod
    def class_meth(cls):
        return math.pi


class C(A, B):
    pass


ser = Serializer.create_serializer('json')

var = 15
var_ser = ser.dumps(var)
var_des = ser.loads(var_ser)
print(var_des)

C_ser = ser.dumps(C)
C_des = ser.loads(C_ser)

c = C(1, 2)
c_ser = ser.dumps(c)
c_des = ser.loads(c_ser)

print(c_des)
print(c_des.x)
print(c_des.my_sin(10))
print(c_des.prop)
print(C_des.stat())
print(c_des.class_meth())

func = lambda x: x*x
func_ser = ser.dumps(func)
n = ser.loads(func_ser)
print(n(3))


f = C(1, 2)
print(f.my_sin(11))
