msg = input("Please enter the message: ")

wantsToSave = input("Do you want to save it?\nyes/no\n")

if wantsToSave == "yes":
    name = input("Please enter name of file: ")
    with open(name + ".txt", "a+") as f:
        f.write(msg)
    f.close()

else:
    print("no save")
