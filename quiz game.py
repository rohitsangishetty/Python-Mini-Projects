
print("Welcome to the computer quiz!")

playing = input("Would you like to play? ")


if playing.lower() != 'yes':
    quit()

print("Alright, let's play!")
score = 0

#question 1
answer = input("What does CPU stand for? ")
if answer == "central processing unit":
    print("Correct!")
    score += 1
else:
    print('Incorrect!')

#question 2
answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print("Correct!")
    score += 1
else:
    print('Incorrect!')

#question 3
answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
  
#question 4
answer = input("What does PSU stand for? ")
if answer.lower() == "power supply":
    print("Correct!")
    score += 1
else:
    print('Incorrect!')

print(f'You got', str(score), 'points!!')
print(f"That means you got a ", str(score/4*100), "%")