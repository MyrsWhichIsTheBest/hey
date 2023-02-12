while True:
    x = input()
    y = int(input())

    if x == "exit":
        break
    replies = {
        1: f"Equal",
        2: f"{x} is larger",
        3: f"{y} is larger"
    }
    if int(x) > y:
        print(replies[2])
    elif y > int(x):
        print(replies[3])
    else:
        print(replies[1])
