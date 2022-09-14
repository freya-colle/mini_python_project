pwd = input("What is the master password? ")

def add():
    new_pwd = input("What is the new master password? ")
    with open("passwords.txt", "a") as f:
        f.write(new_pwd)
    print("Finished adding password")
def view():
    print("Viewed password: ")
    with open("passwords.txt", "r") as f:
        for line in f.readlines():
            print(line)
    

while True:
    mode = input("Would you like to add a new password or view the master password? (add/view) or q to quit").lower()
    if mode == "q":
        break

    if mode == "add":
        add()
    elif mode == "view":
        view()
    else:
        print("Invalid Input")
        continue
