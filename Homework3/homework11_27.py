# Marianel Liga
# PSID 1394330
# Homework 11.27

player_dict = {}

sorted_list_keys = []


# Define the function sortDictKeys().

def sortDictKeys():
    # Sort the dictionary keys and store them into a

    # list, then return that list.

    sorted_list_keys = sorted(player_dict.keys())

    return sorted_list_keys


# (3)

# Define the function outputRoster().

def outputRoster():
    # Call the function sortDictKeys() to get the sorted

    # list of dictionary keys.

    sorted_list_keys = sortDictKeys()

    print("ROSTER")

    # Traverse the list of keys.

    for i in sorted_list_keys:
        # Display jersey number and player's rating

        # sorted by jersey number.

        print("Jersey number: " + str(i)

              + ", Rating: " + str(player_dict[i]))


# (4)

# Define the function addPlayer().

def addPlayer():
    # Prompt the user to enter a jersey number.

    print("Enter a new player's jersey number:")

    jersey_num = int(input())

    # Check if the number entered is valid or not.

    # If not, then again ask the user to enter jersey

    # number.

    while ((jersey_num < 0) or (jersey_num > 99)):
        print("Invalid Jersey Number! Please " +

              "enter again!")

        print("Enter a new player's jersey number:")

        jersey_num = int(input())

    # Prompt the user to enter player's rating.

    print("Enter the player's rating:")

    player_rating = int(input())

    # Check if the number entered is valid or not.

    # If not, then again ask the user to enter

    # player's rating.

    while ((player_rating < 1) or (player_rating > 9)):
        print("Invalid Rating! Please enter again!")

        print("Enter the player's rating:")

        player_rating = int(input())

    # Update the dictionary with new entry.

    player_dict.update({jersey_num: player_rating})


# (5)

# Define the function removePlayer().

def removePlayer():
    # Prompt the user to enter a jersey number.

    print("Enter a jersey number:")

    jersey_num = int(input())

    # Check if the number entered is valid or not.

    # If not, then again ask the user to enter jersey

    # number.

    while ((jersey_num < 0) or (jersey_num > 99)):
        print("Invalid Jersey Number! Please " +

              "enter again!")

        print("Enter a jersey number:")

        jersey_num = int(input())

    # If the entered jersey number is present in the

    # dictionary, then delete the current key, value

    # pair in the dictionary.

    if jersey_num in player_dict.keys():
        del player_dict[jersey_num]


# (6)

# Define the function updatePlayer().

def updatePlayer():
    # Prompt the user to enter a jersey number.

    print("Enter a jersey number:")

    jersey_num = int(input())

    # Check if the number entered is valid or not.

    # If not, then again ask the user to enter jersey

    # number.

    while ((jersey_num < 0) or (jersey_num > 99)):
        print("Invalid Jersey Number! Please " +

              "enter again!")

        print("Enter a jersey number:")

        jersey_num = int(input())

    # Prompt the user to enter a player's rating.

    print("Enter a new rating for player:")

    player_rating = int(input())

    # Check if the number entered is valid or not.

    # If not, then again ask the user to enter player's

    # rating.

    while ((player_rating < 1) or (player_rating > 9)):
        print("Invalid Rating! Please enter again!")

        print("Enter a new rating for player:")

        player_rating = int(input())

    # Update the required key, value pair in the

    # dictionary.

    player_dict[jersey_num] = player_rating


# (7)

# Define the function outputPlayerAboveRating().

def outputPlayerAboveRating():
    # Prompt the user to enter a rating.

    print("Enter a rating:")

    rating = int(input())

    # Check if the number entered is valid or not.

    # If not, then again ask the user to enter a rating.

    while ((player_rating < 1) or (player_rating > 9)):
        print("Invalid Rating! Please enter again!")

        print("Enter a rating:")

        rating = int(input())

    print("ABOVE 5")

    # Call the function sortDictKeys() to get the sorted

    # list of keys of dictionary.

    sorted_list_keys = sortDictKeys()

    # Traverse the list of keys.

    for i in sorted_list_keys:

        # If the current rating in the dictionary is

        # greater than the entered rating.

        if (player_dict[i] > rating):
            # Display the current player's jersey number

            # and rating.

            print("Jersey number: " + str(i)

                  + ", Rating: " + str(player_dict[i]))


# (1)

# Start a for loop from 1 to 6.

for i in range(1, 6):

    # Prompt the user to enter player's jersey number.

    print("Enter player " + str(i) + "'s jersey number:")

    jersey_num = int(input())

    # Check if the number entered is valid or not.

    # If not, then again ask the user to enter jersey

    # number.

    while ((jersey_num < 0) or (jersey_num > 99)):
        print("Invalid Jersey Number! Please " +

              "enter again!")

        print("Enter player " + str(i)

              + "'s jersey number:")

        jersey_num = int(input())

    # Prompt the user to enter a player's rating.

    print("Enter player " + str(i) + "'s rating:")

    player_rating = int(input())

    # Check if the number entered is valid or not.

    # If not, then again ask the user to enter player's

    # rating.

    while ((player_rating < 1) or (player_rating > 9)):
        print("Invalid Rating! Please enter again!")

        print("Enter player " + str(i) + "'s rating:")

        player_rating = int(input())

    print()

    # Add the player rating at key (jersey_num) in the

    # dictionary player_dict.

    player_dict[jersey_num] = player_rating

# Call the function outputRoster() to display player's

# details.

outputRoster()

print()

# (2)

# Start a while loop.

while (True):

    # Display menu of choices.

    print("MENU")

    print("a - Add player")

    print("d - Remove player")

    print("u - Update player rating")

    print("r - Output players above a rating")

    print("o - Output roster")

    print("q - Quit")

    print()

    # Prompt the user to enter a choice.

    print("Choose an option:")

    user_choice = input()

    print()

    # If the user's choice is a, then call the function

    # addPlayer().

    if (user_choice == 'a'):

        addPlayer()



    # If the user's choice is d, then call the function

    # removePlayer().

    elif (user_choice == 'd'):

        removePlayer()



    # If the user's choice is u, then call the function

    # updatePlayer().

    elif (user_choice == 'u'):

        updatePlayer()



    # If the user's choice is r, then call the function

    # outputPlayerAboveRating().

    elif (user_choice == 'r'):

        outputPlayerAboveRating()



    # If the user's choice is o, then call the function

    # outputRoster().

    elif (user_choice == 'o'):

        outputRoster()



    # If the user's choice is q, then break the loop.

    elif (user_choice == 'q'):

        break

    print()