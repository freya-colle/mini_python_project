print("Welcome to the computer quiz game")

playing = input("Press y to play and n to exit. ")

if (playing.lower() == "n"):
    quit();
print("Let's play")
score = 0


answer = input("What does CPU stand for? ")

if (answer.lower() == "central processing unit"):
    print("Correct")
    score += 1
else:
    print("Wrong")


answer = input("What does RAM stand for? ")

if (answer.lower() == "random access memory"):
    print("Correct")
    score += 1

else:
    print("Wrong")

answer = input("What does GPU stand for? ")

if (answer.lower() == "graphic processing unit"):
    print("Correct")
    score += 1

else:
    print("Wrong")

answer = input("What does DA stand for? ")

if (answer.lower() == "data analytics"):
    print("Correct")
    score += 1

else:
    print("Wrong")

print(f"You got {score/4*100}%.")