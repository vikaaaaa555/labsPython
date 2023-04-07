import calculate
import constans
from pathlib import WindowsPath
from wsl_pathlib.path import WslPath


def open_file(path: WindowsPath) -> str:
    with path.open() as f:
        text = f.read()

    return text

def main():
    # text = input("Input some text: ")
    w = WslPath("C:\\Users\\Viktoriya\\Desktop\\example.txt")

    print(open_file(w))






    #print(calculate.all_sentences(f))


if __name__ == "__main__":
    main()