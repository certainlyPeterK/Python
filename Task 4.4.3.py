def task_443():
    ans = input("Как твои дела?\n")
    match ans:
        case "хорошо" | "нормально" | "отлично":
            print("☻")
        case "плохо" | "не хорошо" | "...":
            print("☹")
        case _:
            print(":|")
