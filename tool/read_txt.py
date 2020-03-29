def read_txt(filename):
    with open("../data/"+filename, "r", encoding="utf-8")as f:
        return f.readlines()

if __name__ == '__main__':
    print(read_txt("login.txt"))
    print("--" * 50)
    """
        需求：[(),()]
    """
    arr = []
    for data in read_txt("login.txt"):
        arr.append(tuple(data.strip().split(",")))
    print(arr[1::])