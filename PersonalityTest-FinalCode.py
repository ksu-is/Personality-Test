total_questions = 0
personality_one = 0
personality_two = 0
personality_three = 0

your_name = input("Please enter your name: ").title()
print("Welcome, " + your_name + "! Please answer these series of questions to determine if you are an introvert or an extrovert!")


qDone = False
while qDone == False:
    question1 = input("Question 1: How big is your friend group? \n A) Less than 10. I prefer quantity over quality. \n B) I have a few different friend groups. \n C) I make friends everywhere I go! \n Enter your answer: ")
    if question1.upper() == "A":
        personality_one = personality_one + 1
        qDone = True
        
    elif question1.upper() == "B":
        personality_two = personality_two + 1
        qDone = True
        
    elif question1.upper() == "C":
        personality_three = personality_three + 1
        qDone = True

    else:
        print("Invalid entry. Please enter A, B, or C")


qDone = False
while qDone == False:
    question2 = input("Question 2: You've had a tough day at work. What's your idea of unwinding? \n A) My bed, my pet, and a TV show. \n B) Dinner and a movie with a close friend. \n C) Going out to grab a drink with a group of friends. \n Enter your answer: ")
    if question2.upper() == "A":
        personality_one = personality_one + 1
        qDone = True
        
    elif question2.upper() == "B":
        personality_two = personality_two + 1
        qDone = True
        
    elif question2.upper() == "C":
        personality_three = personality_three + 1
        qDone = True

    else:
        print("Invalid entry. Please enter A, B, or C")


qDone = False
while qDone == False:
    question3 = input("Question 3: At a social event, where do you tend to hang out? \n A) I keep to myself and you can usually find me in the corner. \n B) I mingle with my friends and hang around the food table. \n C) I'm the center of attention! You can find me on the dance floor. \n Enter your answer: ")
    if question3.upper() == "A":
        personality_one = personality_one + 1
        qDone = True
        
    elif question3.upper() == "B":
        personality_two = personality_two + 1
        qDone = True
        
    elif question3.upper() == "C":
        personality_three = personality_three + 1
        qDone = True

    else:
        print("Invalid entry. Please enter A, B, or C")


qDone = False
while qDone == False:
    question4 = input("Question 4: You've just met someone new. How would they describe you? \n A) Shy and reserved \n B) Friendly, but calm \n C) Outgoing, talkative, and friendly \n Enter your answer: ")
    if question4.upper() == "A":
        personality_one = personality_one + 1
        qDone = True
        
    elif question4.upper() == "B":
        personality_two = personality_two + 1
        qDone = True
        
    elif question4.upper() == "C":
        personality_three = personality_three + 1
        qDone = True

    else:
        print("Invalid entry. Please enter A, B, or C")


qDone = False
while qDone == False:
    question5 = input("Question 5: You and a coworker have a disagreement. How do you react? \n A) I let them tell me why I'm wrong and I never bring it up again! \n B) I become quiet in the moment but bring the problem back up later after I have processed my thoughts.  \n C) I don't hold back my thoguhts. Better to get it all out there right away!! \n Enter your answer: ")
    if question5.upper() == "A":
        personality_one = personality_one + 1
        qDone = True
        
    elif question5.upper() == "B":
        personality_two = personality_two + 1
        qDone = True
        
    elif question5.upper() == "C":
        personality_three = personality_three + 1
        qDone = True

    else:
        print("Invalid entry. Please enter A, B, or C")


qDone = False
while qDone == False:
    question6 = input("Question 6: As a child, were you called shy often? \n A) All the time!!! \n B) Occasionally.  \n C) No, never! I was a social butterfly. \n Enter your answer: ")
    if question6.upper() == "A":
        personality_one = personality_one + 1
        qDone = True
        
    elif question6.upper() == "B":
        personality_two = personality_two + 1
        qDone = True
        
    elif question6.upper() == "C":
        personality_three = personality_three + 1
        qDone = True

    else:
        print("Invalid entry. Please enter A, B, or C")


qDone = False
while qDone == False:
    question7 = input("Question 7: You're really busy at work and a colleague is telling you their life story and personal woes. You: \n A) Don't dare to interupt them and just listen. \n B) Listen, but only with half an ear.  \n C) Interupt and explain that you are really busy at the moment. \n Enter your answer: ")
    if question7.upper() == "A":
        personality_one = personality_one + 1
        qDone = True
        
    elif question7.upper() == "B":
        personality_two = personality_two + 1
        qDone = True
        
    elif question7.upper() == "C":
        personality_three = personality_three + 1
        qDone = True

    else:
        print("Invalid entry. Please enter A, B, or C")


qDone = False
while qDone == False:
    question8 = input("Question 8: You crack a joke at work but nobody seems to have noticed. You: \n A) Think it's for the best - it was a lame joke anyway. \n B) Try again a bit later with one of your colleagues. \n C) Keep repeating the punchline until they pay attention. \n Enter your answer: ")
    if question8.upper() == "A":
        personality_one = personality_one + 1
        qDone = True
        
    elif question8.upper() == "B":
        personality_two = personality_two + 1
        qDone = True
        
    elif question8.upper() == "C":
        personality_three = personality_three + 1
        qDone = True

    else:
        print("Invalid entry. Please enter A, B, or C")


qDone = False
while qDone == False:
    question9 = input("Question 9: During dinner the discussion moves to a subject which you know absolutely nothing about. You: \n A) Don't dare open your mouth for fear of looking silly. \n B) Listen and ask periodic questions. \n C) Attempt to change the topic of discussion. \n Enter your answer: ")
    if question9.upper() == "A":
        personality_one = personality_one + 1
        qDone = True
        
    elif question9.upper() == "B":
        personality_two = personality_two + 1
        qDone = True
        
    elif question9.upper() == "C":
        personality_three = personality_three + 1
        qDone = True

    else:
        print("Invalid entry. Please enter A, B, or C")


qDone = False
while qDone == False:
    question10 = input("Question 10: How do you feel about public speaking and presentations? \n A) I DREAD IT!! I hate being the center of attention!!! \n B) Meh. I'd rather not but I guess it has to be done. \n C) I get a sense of pride from sharing my work with an audience! \n Enter your answer: ")
    if question10.upper() == "A":
        personality_one = personality_one + 1
        qDone = True
        
    elif question10.upper() == "B":
        personality_two = personality_two + 1
        qDone = True
        
    elif question10.upper() == "C":
        personality_three = personality_three + 1
        qDone = True

    else:
        print("Invalid entry. Please enter A, B, or C")

#Comment these 3 print statements out later. These are just to check the counts for now.
print("Personality One = " + str(personality_one))
print("Personality Two = " + str(personality_two))
print("Personality Three = " + str(personality_three))

if personality_one > personality_two and personality_one > personality_three:
    print(your_name + "," + "your result is: INTROVERT!")
elif personality_two > personality_one and personality_two > personality_three:
    print(your_name + "," + "your result is: AMBIVERT!")
elif personality_three > personality_one and personality_three > personality_two:
    print(your_name + "," + "your result is: EXTROVERT!")
elif personality_one == personality_two:
    print(your_name + "," + "your result is: IN BETWEEN INTROVERT AND AMBIVERT")
elif personality_two == personality_three:
    print(your_name + "," + "your result is: IN BETWEEN AMBIVERT AND EXTROVERT")
elif personality_one == personality_three:
    print(your_name + "," + "your result is: AMBIVERT!")
elif personality_one == personality_two and personality_one == personality_three:
    print(your_name + "," + "your result is: AMBIVERT!")

#Print Percentages of Each Category (Introvert, Ambivert, Extrovert)
print("You are " + str(personality_one / 10 * 100) + "% Introvert.")
print("You are " + str(personality_two / 10 * 100) + "% Ambivert.")
print("You are " + str(personality_three / 10 * 100) + "% Extrovert.")

#A = Introvert
#B = Ambivert (in between)
#C = Extrovert
