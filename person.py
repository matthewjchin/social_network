class Person:

    # Initialize the contents of each user
    def __init__(self, username, password, statusUpdates, allFriends):
        self._username = username
        self._password = password
        self._updates = statusUpdates
        self._friends = allFriends

    # Get the username of the user and return it
    def getUsername(self):
        return self._username

    # Get the user's password and return it
    def getPassword(self):
        return self._password

    # Get the user's friends' messages and return it
    def getStatus(self):
        return self._updates

    # Get the user's friends and return it
    def getAllFriends(self):
        return self._friends

    def __str__(self):
        return("Username: ", self._username, "\n",
               "Password: ", self._password, "\n",
               "My Updates: ", self._updates, "\n",
               "My Friends: ", self._friends)
