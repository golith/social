# File     : hensy009_social.py
# Author   : Scot Henderson
# Stud ID  : 110010390
# Email ID : hensy009
# Description : A simple social profile managing program
# This is my own work as defined by theUniversity's Academic Misconduct Policy.

import profile
import list_function

def read_file(filename, profile_list):
    # open the file in read mode
    with open(filename, mode="r") as infile:
        # get each line one at a time unti the end
        index = 0
        for line in infile:
            index += 1
            # get details from the first line and split up the result
            word = line.split()
            givenName = word[0]
            familyName = word[1]
            email = word[2]
            gender = word[3]

            # get next line
            line = infile.readline()

            # strip the new line character
            status = line.strip("\n")
            
            # create new profile object with the details retrieved from the file this pass
            thisProfile = profile.Profile(givenName, familyName, email, gender, status)

            # append this object to the profile_list
            profile_list = list_function.insert_value(profile_list, thisProfile, index)

            # get next line to establish friend count
            line = infile.readline()

            # test to see if there are friends and if so add each friend to the profile
            if int(line) > 0:
                for allFriends in range(0,int(line)):
                    # get next line
                    line = infile.readline()
                    
                    # declare a variable to hold the friend variable
                    thisFriend = line.strip("\n")

                    # get this Friends email address and add to friends List
                    thisProfile.add_friend(thisFriend)
    print(profile_list)
    return profile_list

def display_summary(profile_list):
    # loop thorugh each object in the profile list
    for eachProfile in profile_list:
        # print to screen in the format required by the specifications
        print("---------------------------------------------------------------------------")
        display_profile(eachProfile)
    
    # nothing to see here, move along, move along :)
    return

def find_profile(profile_list, email):
    index = list_function.find(profile_list, email)

    return index

def add_profile(profile_list):
    # get an email address to add to the profile list
    email = input("\nPlease enter email address: ")

    # Check if email address exist
    index = find_profile(profile_list, email)
    
    # if the email address does not exist then go ahead and ask for profile data
    if index == -1:
        # Add new profile
        givenName = input("Please enter given name: ")
        familyName = input("Please enter family name: ")
        gender = input("Please enter gender: ")
        status = input("Please enter status: ")

        # Create object
        thisProfile = profile.Profile(givenName, familyName, email, gender, status)
        length = list_function.length(profile_list)
        # use INSERT_VALUE from list_function to update profile
        profile_list = list_function.insert_value(profile_list, thisProfile, length+1)
        
        # print the success of the operation
        print("\nSuccessfully added", email, "to profiles.")

    else:
        # there is already a profile and user can not add another profile 
        # with the same address
        print('\n' + email + " already exists in profiles.\n")

    return profile_list


def remove_profile(profile_list):
    # get an email address to add to the profile list
    email = input("\nPlease enter email address: ")

    ## get the index postion
    index = find_profile(profile_list, email)

    # if the email address does exist then go ahead and delete it from profile data
    if index > -1:

        # find the name in each profile and remove the account
        for profile in profile_list:

            #check if a friend in this profile
            test = profile.is_friend(email)

            # if is_friend is TRUE then delete
            if test == True:
                profile.remove_friend(email)

        # use REMOVE_VALUE from list_function to update profile
        profile_list = list_function.remove_value(profile_list, index)

        print("\nSuccessfully removed", email, "from profiles.\n")

    else:
        # there is no profile to find in the list to remove
        print("\n" + email + " is not found in profiles.\n") 

    return profile_list

def write_to_file(filename, profile_list):
    # open the file in write mode
    with open(filename, 'w') as outfile:
        # loop through the profile objects in the profile list
        for eachProfile in profile_list:
            # write each proflie to the file declared via the function argument
            # using the __str_ function declared in Profile module
            outfile.write(str(eachProfile))

    # close the file
    outfile.close()
    return

###########################
## CUSTOM FUNCTIONS START##
###########################

def user_choice():
    # get user choice at the start of the program
    select = input("\nPlease enter choice [summary|add|remove|search|update|quit]: ")

    # If the input is not in the list of available commands then let the user know
    # and then try again.  Keep doing this until we get a valid response
    while select not in select_list:
        print("\nNot a valid command - please try again.")
        select = input("\nPlease enter choice [summary|add|remove|search|update|quit]: ")

    # return a valid user choice
    return select

def user_choice2(email):
    # define the users full name via a custom function
    fullname = get_full_name(profile_list, email)

    # declare a variable to hold the string to print input request
    string = "\n\nUpdate " + fullname + " "
    string += "[status|add_friend|remove_friend]: "

    # get user choice
    subSelect = input(string)

    # test if user choice is in the list of valid choices and
    # if not tell the user that you are going back to the main menu
    if subSelect not in select_list2:
        print("\nNot a valid command - returning to main menu.\n")

    return subSelect

def display_details():
    # Display the details of the programmer as per assignment specifications
    print("File     : hensy009_social.py")
    print("Author   : Scot Henderson")
    print("Stud ID  : 110010390")
    print("Email ID : hensy009")
    print("Description : A simple social profile managing program")
    print("This is my own work as defined by theUniversity's Academic Misconduct Policy.")
    
    return

def display_profile(profile):
    # printing objects instead of using reverse string method from list_function.py
    print(profile.get_given_name() + " ", end ="")
    print(profile.get_family_name(), end ="")
    print(" (" + profile.get_gender(), end ="")
    print(" | " + profile.get_email() + ")\n", end ="")
    print("- " + profile.get_status())

    # if there are friends in the list then print these as well             
    if int(profile.get_number_friends()) > 0:
        print("- Friends (" + str(profile.get_number_friends()) + "):")
        for thisFriend in profile.get_friends_list():
            fullName = get_full_name(profile_list, thisFriend)
            print("    " + fullName)
    
    # otherwise print this statement
    else:
        print("- No friends yet...")
    return

def get_name(profile_list, email):
    # get index postion according to email
    index = find_profile(profile_list, email)

    # get the firstname of the single profile
    details = profile_list[index]

    # get the first name and make the first character a capital
    firstName = details.get_given_name().title() 

    return firstName

def get_full_name(profile_list, email):
    # get index postion according to email
    index = find_profile(profile_list, email)

    # get the details of the profile according to the email passed as ARGS
    details = profile_list[index]

    # concatenate given and family name 
    fullName = details.get_given_name() + " " + details.get_family_name()

    # capitalise the first character of both parts of the name
    fullName = fullName.title()

    return fullName

## CUSTOM FUNCTIONS END ##

###################
## START PROGRAM ##
###################

# set variable to use in the program

# we want the program to run at the begining so set it to true
start = True

# define the lists that are to use to validate the user choices
select_list = ["summary","add","remove","search","update","quit"]
select_list2 = ["status","add_friend","remove_friend"]

# declare and empty list called profile_list
profile_list = []

# read the information from profiles.txt as objects
profile_list = read_file("profiles.txt", profile_list)

# display the programmers details as per assingment specification
display_details()

# get the user choice at the start of the program
select = user_choice()

# Start the program after user selects a valid choice
# we also want to test for true as when user quits at the end we set start to FALSE
while select in select_list and start == True:

    # use IF statements to repsond to the user choice
    if select == "summary":
        # make it pritty as per assingment specification
        print("===========================================================================")
        print("Profile Summary")
        print("===========================================================================")
        
        # call the function to print to screen the profile list
        display_summary(profile_list)

        # make it pritty as per assingment specification
        print("---------------------------------------------------------------------------")
        print("===========================================================================")
        
        # ask user what they want to do next
        select = user_choice()

    elif select == "add":
        # call the function to add a new profile
        profile_list = add_profile(profile_list)

        # ask user what they want to do next
        select = user_choice()

    elif select == "remove":
        # call the function to remove a profile
        profile_list = remove_profile(profile_list)

        # ask user what they want to do next
        select = user_choice()

    elif select == "search":
        # get the email address that the user wants to search
        email = input("\nPlease enter email address: ")

        # get the index position of the email address
        index = find_profile(profile_list, email)

        # if there is a result
        if index > -1:
            # get the profile that belongs to the email address
            profile = profile_list[index]
            # print the resulting profile according to the email address
            print("\n")
            display_profile(profile)

        else:
            #otherwise there was no email found in the profile list
            print("\n" + email + " is not found in profiles.\n")

        # get the user choice of what they want to do next
        select = user_choice()

    elif select == "update":
        # get the email address of the user to update
        email = input("\nPlease enter email address to update: ")

        # get the index position in the profile list according to the email
        index = find_profile(profile_list, email)

        # test to see if there is an email address
        if index > -1:
            
            # now we need to get the users choice to see what to do next
            subSelect = user_choice2(email)
            profile = profile_list[index]

            # get the first name of the user via a function call
            firstName = get_name(profile_list, email).title()
            # get the first and last name of the user via a function call
            fullName = get_full_name(profile_list, email).title()

            # use IF statements to repsond to the user choice from the subSelect menu
            if subSelect == "status":
                # get new status
                update = input("\nPlease enter status update: ")

                # update the old status
                profile.set_status(update)

                print("\nUpdated status for " + fullName + ":")
                # print profile with updated status
                display_profile(profile)

            if subSelect == "add_friend":
                # get the email address of the friend the user wants to add
                friendEmail = input("\nPlease enter email address of friend to add: ")

                # get the index position of the friends email
                test = find_profile(profile_list, friendEmail)

                # get the first name of the friend just added via a function call
                friendFirstName = get_name(profile_list, friendEmail)

                # if the friends email does exist in the profile list
                if test > -1:
                    # add the friend to the users profile via the ADD_FRIEND function
                    emailToAdd = profile.add_friend(friendEmail)

                    # Test to see if the add_friend returned a true result
                    if emailToAdd is True:
                        # get the first name of the friend just added via a function call                        
                        
                        # print out a successful result
                        print("\nAdded", friendFirstName, "updated profile is:")

                        # print profile
                        display_profile(profile) 

                    else:
                        # let thm know that the person is alread a friend as it is false
                        print("\n" + friendFirstName + " is already a friend.\n")
                
                # the profile does not exist
                else:
                    print("\n" + friendEmail + " is not found in profiles.\n")
            
            if subSelect == "remove_friend":
                # get the email address of the friend the user wants to remove
                friendEmail = input("\nPlease enter email address of friend to remove: ")

                # get the index position of the friends email
                test = find_profile(profile_list, friendEmail)
                
                if test > -1:
                    # add the friend to the users profile via the REMOVE_FRIEND function
                    emailToRemove = profile.remove_friend(friendEmail)                    

                    if emailToRemove is True:
                        # print successful removal and the friend first name that is removed
                        print("\nRemoved", friendEmail, "updated profile is:")

                        # print the profile we are working on to show change
                        display_profile(profile)
                    
                    else:
                        # if the test is FALSE then it means the email is not on the users friends list
                        # print("\n" + friendEmail + " is not", profile_list[index].get_given_name().title() + "'s friend.")
                        print("\n" + friendEmail + " is not " + firstName + "'s friend.\n")
                else:
                    # the profile the user wants to remove is not found in the profile list
                    # print("\n" + friendEmail + " is not found in profiles.")   
                    print("\n" + friendEmail + " is not " + firstName + "'s friend.\n")
        # the profile that the user wants to call to update does not exist
        else:
            print("\n" + email + " is not found in profiles.\n")

        # get the user choice of what they want to do next
        select = user_choice()

    elif select == "quit":
        # when the user has finished with the program write the profile list to file
        write_to_file("new_profiles.txt", profile_list)

        # let the user know that the program has terminated
        print("\n\n-- Program terminating --")

        # set the start of the program to FALSE to get the WHILE loop to stop
        start = False
