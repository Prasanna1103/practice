import re

def main():
    data = input("Data: ")
    if is_valid_data(data):
        print("Valid")
    else:
        print("Invalid")

# dates
# 3-12-2024
# 03-12-2024
# 3-12-24
# 03-12-24

def is_valid_data(data):
    pattern = re.compile("(0?[1-9]|[12][0-9]|3[01])-(\d|\d{2})-(\d{2}|\d{4})$")
    groups = pattern.match(data)
    if groups:
        print(groups.group(1))
        print(groups.group(2))
        print(groups.group(3))
        return True
    return False

    

def is_valid_re(s):
    if len(s) >= 2 and len(s) <= 6:
        pattern = re.compile("[a-zA-Z][a-zA-Z]+([1-9][0-9]+)*$")
        if pattern.match(s):
            return True
    return False

def is_valid(s):
    if len(s) < 2 or len(s) > 6:
        return False
    if not s[0].isalpha() or not s[1].isalpha():
        return False
    num_start_i = 0
    for i in range(2, len(s)):
        if s[i].isalpha():
            continue
        elif s[i].isdigit():
            num_start_i  = i
            break
    if num_start_i != 0:
        if s[num_start_i] == "0":
            return False
        print(s[num_start_i:])
        if not s[num_start_i:].isdigit():
            return False
    
    return True

main()
#s = "cse500"
#print(s[2:])