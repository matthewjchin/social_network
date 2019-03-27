from person import Person
import string
users = []
allContents = []


def incorrectInput():  # only if user gives invalid input or if incorrect password
    print("Please try again. ")
    ans = input("Please type 'Y' for yes or 'N' for no to continue: ")
    if ans == 'Y':
        print("Sending you back")
        main()
    elif ans == 'N':
        quit()
    else:
        ans = input("Please type 'Y' for yes or 'N' for no to continue: ")


def main():
    # Read through each line in the text file of the network.txt file
    openFile = open("/Users/mattjchin/Desktop/python_work/project4/network.txt").readlines()
    count = 0  # Count variable used for first for loop
    for line in openFile:  # Reads through each line in the text file
        line = line.strip(",\n")
        newline = line.split(", ")
        username = newline[0]  # for each line the string at position 0 is the username
        password = newline[1]  # for each line the string at position 1 is the password
        messages = []  # initialize a new list for every user and the user's messages
        friends = []  # initialize a new list for every user and the user's friends
        count = 3  # Skip over the item at position 2 of every line, which is the word "messages"
        while newline[count] != "friends":
            messages.append(newline[count])  # Adds the message at that position into the messages list
            count += 1  # Adds 1 to the count variable after THIS iteration
            # print("Hi")  # Used to debug
        count += 1
        while count < len(newline):
            friends.append(newline[count])  # Adds the friend at that position into the friends list
            count += 1  # Adds 1 to the count variable after THIS iteration

        person = Person(username, password, messages, friends)
        allContents.append(person)

    loginname = input("Username: ")
    password = input("Password: ")

    newcount = 0
    cond = True  # Set True/False condition
    while cond:  # while loop used as a condition for the program to run through multiple iterations, not just one
        for x in allContents:
            if x.getUsername() == loginname:
                if x.getPassword() == password:
                    # print("all is cool")
                    # saved = x
                    # print("Password is correct. ")
                    # Options
                    ans = int(input("Please enter your option: \n"
                                    "1 - Print all of my Friends \n"
                                    "2 - Print my messages/status updates \n"
                                    "3 - Post a new messages/status update \n"
                                    "4 - Post all my friend's messages/status updates \n"
                                    "5 - Add a friend \n"
                                    "6 - Logout (Switch user) \n"
                                    "7 - Exit the Social Network \n"
                                    "Insert option here: "))
                    if ans == 1:
                        print(x.getAllFriends())  # Prints the list of the user's friends
                    elif ans == 2:
                        print(x.getStatus())  # Prints the messages the user put
                    elif ans == 3:  # Allows user to input own message
                        userMessage = input("Enter your message: ")
                        x.getStatus().append(userMessage)  # Add new message in user's own message list
                        print(x.getStatus())
                    elif ans == 4:
                        for n in x.getAllFriends():  # Search for friends
                            for y in allContents:  # Search through the text file
                                if n == y.getUsername():
                                    y.getStatus()
                                    print(str(y.getUsername()) + ": " + str(y.getStatus()))
                    elif ans == 5:  # Add a friend
                        newFr = input("Please input new name of friend: ")
                        x.getAllFriends().append(newFr)  # Add new friend to the friend list
                        print(str(x.getAllFriends()))
                    elif ans == 6:
                        print("You have been successfully logged out. ")
                        loginname = input("Username: ")  # Ask for username
                        password = input("Password: ")   # Ask for password
                    elif ans == 7:  # Write to text file prior to exiting the program
                        rewrite = open("/Users/mattjchin/Desktop/python_work/project4/network.txt", "w")
                        for i in range(len(allContents)):
                            user = []  # initialize a new list
                            user.append(allContents[i].getUsername())
                            user.append(allContents[i].getPassword())
                            user.append("messages")  # puts the word messages
                            sep = ", ".join(allContents[i].getStatus())  # puts all messages in list
                            user.append(sep)
                            user.append("friends")  # puts the word friends
                            sepusers = ", ".join(allContents[i].getAllFriends())  # puts all friends in list
                            user.append(sepusers)
                            haha_users = ", ".join(user)
                            rewrite.write(haha_users + '\n')

                        # while countedit != len(allContents):
                        #     for eachu in allContents:
                        #         rewrite.write(str(eachu.getUsername())+", "+str(eachu.getPassword())
                        #                       + ", messages, " + (str(eachu.getStatus())) + ", friends, "
                        #                       + str(eachu.getAllFriends() + "\n"))
                        print("You have exited the program.")
                        quit()

                    # elif ans == 8:
                    #     print(x.getAllFriends())
                    #     dict = {}
                    #     x.getAllFriends().values()
                    #     count_name = 0  # Initialize a new count variable for each friend
                    #     # for eachfriend in x.getAllFriends():
                    #     #     dict.keys(eachfriend[count_name])
                    #
                    #     search = input("Input the friend you're looking for: ")
                    #     # count_name = 0  # Initialize a new count variable for each friend
                    #     friendmessages = []
                    #     for search in x.getAllFriends():
                    #         for eachname in allContents:
                    #             if search == eachname.getAllFriends():
                    #                 eachname.getStatus()
                    #         print(str(eachname.getUsername()) + ": " + str(eachname.getStatus()))
                    #     # dict = {}
                    #     # dict1 = dict.keys()
                    #     # dict2 = dict.values()
                    #     # print(dict1)
                    #     # print(dict2)
                    #     # search = input("Input the friend you're looking for: ")
                    #     # # for n in dict:
                    #     # #     if search in dict1:
                    #     # #         print(dict2)
                    #     # #     else:
                    #     # #         print("No such friend was found.")
                    #     # if search == y.getUsername():
                    #     #     y.getStatus()
                    #     #     print(y.getUsername(), y.getStatus())
                    #     # else:
                    #     #     print("No such friend was found.")
                    else:  # Only if password is incorrect
                        print("Invalid input. ")  
			# Repeat the comments as applied for first iteration of 7 choices
                        ans = int(input("Please enter your option: \n"
                                        "1 - Print all of my Friends \n"
                                        "2 - Print all messages/status updates \n"
                                        "3 - Post a new messages/status update \n"
                                        "4 - Post all my friend's messages/status updates \n"
                                        "5 - Add a friend \n"
                                        "6 - Logout (Switch user) \n"
                                        "7 - Exit the Social Network \n"
                                        "Insert option here: "))
                        # Repeat the comments for the above menu options
                        if ans == 1:
                            print(x.getAllFriends())
                        elif ans == 2:
                            print(x.getStatus())
                        elif ans == 3:
                            userMessage = input("Enter your message: ")
                            x.getStatus().append(userMessage)
                            print(x.getStatus())
                        elif ans == 4:
                            for n in x.getAllFriends():
                                for y in allContents:
                                    if n == y.getUsername():
                                        y.getStatus()
                                        print(y.getUsername(), y.getStatus())
                        elif ans == 5:  # adds to the list of the user's friends
                            newFr = input("Please input new name of friend: ")
                            x.getAllFriends().append(newFr)
                            print(x.getAllFriends())
                        elif ans == 6:
                            # Logs out of the current user, takes back to ask input for username and password
                            print("You have been successfully logged out. ")
                            loginname = input("Username: ")
                            password = input("Password: ")
                        elif ans == 7:
                            # writeToFile = open("C:/Users/mattc/Desktop/python_work/project4/network.txt", "a+")
                            quit()
                        # elif ans == 8:
                        #     quit()

                else:
                    # If password is incorrect
                    print("Incorrect username or password. Please try again. ")
                    incorrectInput()
            elif x.getUsername() != loginname:
                count += 1
            else:
                # Shown only if the username does not show up or is read in the text file or is not found
                print("The username could not be found.")
                main()
    if cond == False:  # if condition is false where there is no username found then the program will go to login menu
        print("No such username exists.")
        main()


main()
