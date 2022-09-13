while True:
    string = input()
    if string == "0":
        break
    arr_str = list(string)
    # [start : end : step]
    if arr_str[::-1] == arr_str:
        print("yes")
    else:
        print("no")