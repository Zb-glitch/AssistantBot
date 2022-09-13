#from assistant import userName


neededFile = ""
contentList = []

# Adding text to the task log
class AddToTaskManager():
    neededFile = input("Please enter the file name: ")
    toAdd = open(neededFile, 'a')
    
    userInfo = toAdd.write(input("What would you like to add to this document? \n") + "\n")

    keepAddingToFile = input("Would you like to add anything else to this file? \n")

    while keepAddingToFile != "No":
        moreUserInfo = toAdd.write(input("What else would you like to add to this file? \n") + "\n")
        askAgain = input("Would you like to add anything else to this file? \n")
        

        if askAgain != "Yes":
            break

    toAdd.close()

        

AddToTaskManager()
print("Okay, I've got everything added to your task log!")


# Reading contents of task log
class ReadTaskLog():
    nav = open(AddToTaskManager.neededFile, 'r')

    fileContents = nav.read()
    print("Here are the tasks listed in your task manager \n" + fileContents)

    nav.close()


ReadTaskLog()

class CreateFile():
     askUser = input("Would you like to create a new text file? \n")

     if askUser == "Yes":
         fileName = input("What would you like to name this file? \n")
         theFileName = fileName + '.txt'

         with open(str(theFileName), 'x') as f:
             f.write("This is your new text file!")

     elif askUser == "No":
         print("Okay, we can work on a text file that's already in this folder")


#class Entertainment():
    #def convo_prompts():
        #print(f"You don't know how excited I am {userName}, you're the first human I get to talk to!")
        #convoStarter = input(f"Now that we have {}")


# Here the program records user responses that aren't already in the current user response library
# Copy + Paste then edit as needed
#class RecordedUserResponses():
    #newUserResponses = []
    #if usersResponse not in doing_prior:
        #newUserResponses = newUserResponses.append(userResponse)

  
      

      