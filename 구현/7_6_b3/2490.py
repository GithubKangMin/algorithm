for _ in range(3):
    a,b,c,d = map(int,input().split())
    list = [a,b,c,d]

    num = list.count(0)

    if num == 0:
        print("E")

    elif num == 1:
        print("A")

    elif num == 2:
        print("B")

    elif num == 3:
        print("C")

    elif num == 4:
        print("D")
