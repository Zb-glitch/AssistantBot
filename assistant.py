from datetime import *
from task_log_classes import AddToTaskManager
from task_log_classes import ReadTaskLog
from task_log_classes import CreateFile

today = date.today()
theTime = datetime.now()

# Initial user interactions
userName = input("Hello there! I'm Bot, your new virtual assistant. Before I get started on the fun stuff, what would you like me to call you? \n")
print(f"It's a pleasure to meet you {userName}!")

botName = input(f"Would you like to give me a new name {userName}? \n")

if botName == "Yes":
    newBotName = input(f"Okay {userName}, what is my new name? \n")
    print(f"Wonderful, I have my very own name now! {newBotName} is an excellent name {userName}, thank you for giving it to me!")


elif botName == "No":
    print(f"Alright {userName}, my name will continue to be Bot!")

else:
    print(f"I'm sorry {userName}, I did not understand your response. Please answer with a yes or a no")


# Function for user to decide of they want to be called by a nickname (NEEDS WORK)
class NickNames():
    wantNickName = ""
    if len(userName) >= 6:
        print(f"I've been thinking {userName}, I like your name but it's a little long")
        wantNickName = input("Do you have any nicknames that you'd like me to call you? \n")

    if wantNickName == "Yes":
        theNickName = input("Alright, what would you like me to call you? \n")
        print(f"Great, instead of {userName} I'll call you {theNickName}!")

        

    elif wantNickName == "No":
        print(f"Alright, I'll continue to call you {userName}!")
        


NickNames()

if NickNames.wantNickName == "Yes":
    starting = print(f"Okay {NickNames.theNickName}, what would you like me to do first? \n")

else:
    starting = print(f"Okay {userName}, what would you like me to do first? \n")

startCommand = input("""I can: \n[1] Remind you of today's date and time \n
                                 [2] Track current or futre tasks and events that you can later check on \n
                                 [3] Perform any calculation you may need \n
                                 [4] Entertain you for a while \n
                                 [5] Create a new text file \n
                                 Which task would you like me to do right now? \n """)

neededFile = ""
contentList = []

# Adding text to the task log
class AddToTaskManager():
    neededFile = input("Please enter the file name(task_log.txt): ")
    toAdd = open(neededFile, 'a')
    
    userInfo = toAdd.write(input("What would you like to add to this document? \n") + "\n")

    keepAddingToFile = input("Would you like to add anything else to this file? \n")

    while keepAddingToFile != "No":
        moreUserInfo = toAdd.write(input("What else would you like to add to this file? \n") + "\n")
        askAgain = input("Would you like to add anything else to this file? \n")
        

        if askAgain != "Yes":
            break

    toAdd.close()


# Reading contents of task log
class ReadTaskLog():
    nav = open(AddToTaskManager.neededFile, 'r')

    fileContents = nav.read()
    print("Here are the tasks listed in your task manager \n" + fileContents)

    nav.close()


# Creating a new text file
class CreateFile():
     askUser = input("Would you like to create a new text file? \n")

     if askUser == "Yes":
         fileName = input("What would you like to name this file? \n")
         theFileName = fileName + '.txt'

         with open(str(theFileName), 'x') as f:
             f.write("This is your new text file!")

     elif askUser == "No":
         print("Okay, we can work on a text file that's already in this folder")


#class GiveDateTime():
class GiveDateTime():
    asking_user = input(f"Would you like to know today's date or time? \n")

    if asking_user == 'Date':
        print(f"Today's date is {today}")

    elif asking_user == 'Time':
        print(f"It is currently {theTime}")

    else:
        print(f"I'm sory {userName}, I didn't understand your response \n")


# First elif statement is executed instead of the if statement. NEEDS WORK
if startCommand == '1':
    print(f"It is currently {theTime} on {today}")
    newStartPrompt = input("""Would you like me to: \n[1] Remind you of today's date and time \n
                                                     [2] Track current or futre tasks and events that you can later check on \n
                                                     [3] Perform any calculation you may need \n
                                                     [4] Entertain you for a while \n
                                                     [5] Create a new text file \n
                                                     Which task would you like me to do right now? \n """)

#elif startCommand == '2':