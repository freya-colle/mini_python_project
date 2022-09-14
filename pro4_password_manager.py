pwd = input("What is the master password? ")

def add():
    new_account = input("Account name: ")
    new_pwd = input("What is the new master password? ")
    with open("passwords.txt", "a") as f:
        f.write(new_account  + ": " + new_pwd  + "\n")
    print("Finished adding password")


def view():
    print("Viewed password: ")
    with open("passwords.txt", "r") as f:
        for line in f.readlines():
            data = line.rstrip()
            account, new_password = data.split(": ")
            print(f"user: {account}, password: {new_password}")
    

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
