import re

def count_substring(string, sub_string):
    qty = 0
    length = len(sub_string)
    for i in range(len(string) - length + 1):
        if sub_string in string[i:i+length]:
            qty += 1
    return qty

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)
