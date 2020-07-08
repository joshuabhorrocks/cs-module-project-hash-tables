def no_dups(s):
    final_str = " "
    split_s = s.split()

    split_s = list(dict.fromkeys(split_s))
    final_str = final_str.join(split_s)
    return final_str


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))