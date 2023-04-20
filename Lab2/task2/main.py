from container import UniqueContainer
import keyboard


def main():
    print("---------------------------------------------------------------------\n"
        "add(arguments) – add one or more elements to the container\n"
        "remove(argument) – delete key from container"
        "find(arguments) – check if the element is presented in the container\n"
        "list – print all elements of container\n"
        "grep(regex) – check the value in the container by regular expression\n"
        "save - save container to file\n"
        "load - load container from file\n"
        "switch – switches to another user\n"
        "q - press 'q' to exit\n"
        "---------------------------------------------------------------------")

    while True:
        username = input("Enter username: ")
        container = UniqueContainer(username)
        while True:
            command = input("Do you want to load data? (y/n) ")
            match command:
                case "y":
                    container.load()
                    break
                case "n":
                    container.load_username()
                    break

        while True:
            command = input("Enter command: ")

            match command.split()[0]:
                case "add":
                    args = command.split()[1:]
                    container.add(*args)
                case "remove":
                    args = command.split()[1]
                    container.remove(args)
                case "find":
                    args = command.split()[1:]
                    container.find(*args)
                case "list":
                    container.list()
                case "grep":
                    pattern = command.split()[1]
                    container.grep(pattern)
                case "save":
                    container.save()
                case "load":
                    container.load()
                case "switch":
                    while True:
                        command = input("Do you want to save data? (y/n) ")
                        match command:
                            case "y":
                                container.save()
                                break
                            case "n":
                                break
                    break
                case "q":
                    while True:
                        command = input("Do you want to save data? (y/n) ")
                        match command:
                            case "y":
                                container.save()
                                break
                            case "n":
                                break
                    return
                case _:
                    print("Unknown command: ", command)


if __name__ == "__main__":
    main()
