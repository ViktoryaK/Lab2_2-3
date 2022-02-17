"""
This is a module which helps to easily navigate through a json file
"""
import json


def reading():
    """
    This function reads a json file, which was created with the twitter2.py.
    """
    print("Please, enter the file you want to explore in the format: name.json")
    inp = input()
    with open(inp, 'r') as file:
        data = json.load(file)
    return data


def user_request_dict():
    print("If you want to see what is inside: Please, input the dictionary key, which value you want to see: ")
    inp = input()
    return inp


def user_request_list(length):
    print(f"If you want to see what is inside: Please, input the list index from 0 to {length}")
    inp = input()
    if int(inp) < 0:
        print("Input correctly")
        return 'bad input'
    return inp


def analyze(data):
    """
    This function analyses the entire json file.
    """
    if type(data) == list:
        try:
            print("We have a list")
            index = user_request_list(len(data))
            if index == "bad input":
                analyze(data)
            else:
                print("We have a list")
                analyze(data[int(index)])
        except IndexError:
            print("Input a right index, please")
            analyze(data)
    elif type(data) == dict:
        try:
            print('We have a dictionary')
            print('Keys:')
            for key in data:
                print(key)
            key = user_request_dict()
            analyze(data[key])
        except KeyError:
            print('Input an existing key. Please.')
            analyze(data)
    else:
        print(data)


if __name__ == "__main__":
    try:
        analyze(reading())
    except Exception:
        print("Input correctly")
