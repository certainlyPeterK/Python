def task_433():
    a = int(input())
    b = int(input())
    c = int(input())
    if a == b and b == c:
        print("Равносторонний")
    elif a == b or b == c or a == c:
        print("Равнобедренный")
    else:
        print("Разносторонний")
