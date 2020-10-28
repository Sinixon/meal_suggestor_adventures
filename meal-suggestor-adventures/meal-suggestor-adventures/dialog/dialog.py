import time  # the time import is used to slow down the dialog. I use the sleep function of it.
import random # import to make a random choice
import sys # import used to write character by character to the console

import user.user as MainCharacter

textColor = "\033[1;32;40m" # variable to set the text color

# this function is used to make the text appear like a text adventure game
# it picks a random number from the array so that the delay is different every time
# this makes it look like the text is actually being typed as a real person
def faketype(words):
  words
  for char in words:
    time.sleep(random.choice([0.3, 0.11, 0.08, 0.07,   0.07, 0.07, 0.06, 0.06, 0.05, 0.01]))
    sys.stdout.write(char)
    sys.stdout.flush()

# this function will display the very first introduction
def displayIntro():
    faketype(textColor + "Hey there! Welcome to Meal Suggestor Adventures.\n")
    faketype("In order to move forward we need to have a main character for this adventure.\n"
             "We would like you to be our main character.\n")
    faketype("To be this, we are going to need a few details from you.\n")
    return getMainCharacterName()


# this function will ask for the users name
# it makes a new variable called mainChracterName and returns it so we can use it in a different class
# the if statement is runned as many times untill the user fills in characters !!!! NOT FINISHED
def getMainCharacterName():
    mainCharacterName : str
    faketype(">>> Please fill in your name: \n")
    mainCharacterName = input()
    if not mainCharacterName:
        getMainCharacterName()
    if mainCharacterName:
        faketype("Welcome " + mainCharacterName + "!\n")
        MainCharacter.set_name(MainCharacter, mainCharacterName)
        return getAgeOfMainCharacter()

# this function will ask for the users age
# I made conditions for the age. It cannot be 0, has to be lower than 99 and cannot be negative
# it will also check if the user filled in integers (whole numbers) instead of characters/a float
def getAgeOfMainCharacter():
    var_check_name = False
    while not var_check_name:
        faketype(">>> Please fill in your age (numbers only): \n")
        mainCharacterAge = input()
        try:
            val = int(mainCharacterAge)
            if 0 < val < 99:
                faketype("Your age is set to " + mainCharacterAge + "\n")
                MainCharacter.set_age(MainCharacter, mainCharacterAge)
                return getSexOfMainCharacter()
            elif val == 0:
                print("I doubt you were just born...")
            elif val >= 99:
                print("You already lived so well, I don't think you need to use this program")
            elif val < 0:
                print("Whatttt, how can you have a negative age?")
        except ValueError:
            print("There is no age on earth that consists of characters...")


# this function will ask for the users sex
# I made conditions for this function. Sex has to be either man or woman. I use the lower function so it doesn't matter if user uses capital letters
# I used a boolean to keep the loop going and repeat the question if the user doesn't meet the required input condition
def getSexOfMainCharacter():
    var_check_sex = False
    while not var_check_sex:
        faketype(">>> Please fill in your sex (man/woman): \n")
        mainCharacterSex = input()
        if mainCharacterSex.lower() == "man" or mainCharacterSex.lower() == "woman":
            mainCharacterSex = mainCharacterSex.lower()
            faketype("Your sex is set to: " + mainCharacterSex + "\n")
            MainCharacter.set_sex(MainCharacter, mainCharacterSex)
            return getActivityLevelOfMainCharacter()
        else:
            print("Are you an alien?")


# this function is used to get the users activity level
# the activity level goes from 1-5
# I used a boolean to keep the loop going and repeat the question if the user doesn't meet the required input condition
# also I used the same function int() to check if the user only filled in an integer
def getActivityLevelOfMainCharacter():
    var_check_activity_level = False
    while not var_check_activity_level:
        faketype(">>> Please fill in your activity level. With 1 being the lowest and 5 the highest: \n")
        mainCharacterActivityLevel = input()
        try:
            val = int(mainCharacterActivityLevel)
            if 0 < val < 6:
                faketype("Your activity level is set to " + mainCharacterActivityLevel + "\n")
                MainCharacter.set_activitylevel(MainCharacter, mainCharacterActivityLevel)
                return getWeightOfMainCharacter()
            else:
                print("That is not a number between 1 and 5 :-(")
        except ValueError:
            print("Do you know the difference between numbers and characters?")


# work in progress
def getWeightOfMainCharacter():
    var_check_weight = False
    while not var_check_weight:
        faketype(">>> Please fill in your weight (in kg): \n")
        mainCharacterWeight = input()
        try:
            val = int(mainCharacterWeight)
            if 0 < val < 250:
                faketype("Your weight is set to " + mainCharacterWeight + "\n")
                MainCharacter.set_weight(MainCharacter, mainCharacterWeight)
                return getHeightOfMainCharacter()
            else:
                #little work in progress but good for now
                print("I can't believe you are that light or so heavy")
        except ValueError:
            print("Come on now... NO CHARACTERS")


# this function is used to get the users height
# I used a boolean to keep the loop going and repeat the question if the user doesn't meet the required input condition
# I don't think anyone will be short than 100cm and taller than 275cm so I used that as the condition
# the int() function is used to check if the user filled in integers
def getHeightOfMainCharacter():
    var_check_height = False
    while not var_check_height:
        faketype(">>> Please fill in your height (in cm): \n")
        mainCharacterHeight = input()
        try:
            val = int(mainCharacterHeight)
            if val > 100 and val < 275:
                faketype("Your length is set to " + mainCharacterHeight + " cm\n")
                MainCharacter.set_height(MainCharacter, mainCharacterHeight)
                return getGoalOfMainCharacter()
            else:
                print("I can't believe this is really your height")
        except ValueError:
            print("You know centimeters are not characters... Right?")

# this function is used to get the users goal
# I made conditions for this function. The goal has to be lose weight/stay at weight/gain weight.
# I use the lower function so it doesn't matter if user uses capital letters
# I used a boolean to keep the loop going and repeat the question if the user doesn't meet the required input condition
def getGoalOfMainCharacter():
    var_check_goal = False
    while not var_check_goal:
        faketype(">>> Please fill in your goal (lose weight/stay at weight/gain weight): \n")
        mainCharacterGoal = input()
        if mainCharacterGoal.lower() == "lose weight" or mainCharacterGoal.lower() == "stay at weight" or mainCharacterGoal.lower() == "gain weight":
            faketype("Your goal is set to " + mainCharacterGoal + "\n\n\n")
            MainCharacter.set_goal(MainCharacter, mainCharacterGoal)
            return calculateBMR(MainCharacter.get_sex(MainCharacter))
        else:
            print("Please choose a valid option")

# this function will calculate the BMR of the user based on his sex
# the formula used is documented in the project template at "Literatuurlijst" under the name Calulator.net
# it returns the calculated BMR within the parameter to the next function
def calculateBMR(check_sex):
    if check_sex == 'man':
        mainCharacterBMR = (10 * (float(MainCharacter.get_weight(MainCharacter)))) \
                           + (6.25 * (float(MainCharacter.get_height(MainCharacter)))) \
                           - (5 * (float(MainCharacter.get_age(MainCharacter)))) + 5
        return calculateCaloriesByActivity(MainCharacter.get_activitylevel(MainCharacter), 1, 1.15, mainCharacterBMR)
    else:
        mainCharacterBMR = (10 * (float(MainCharacter.get_weight(MainCharacter)))) \
                           + (6.25 * (float(MainCharacter.get_height(MainCharacter)))) \
                           - (5 * (float(MainCharacter.get_age(MainCharacter)))) - 161
        return calculateCaloriesByActivity(MainCharacter.get_activitylevel(MainCharacter), 1, 1.15, mainCharacterBMR)

# this function will calculate the calories of the user by activity
# it uses the BMR value as a primary value
# the activity level will make sure the BMR value gets multiplied by 1.15 for the first adding 0.10 per level
# recursion is used in the else statement. The counter X will go on untill it finds the same value as the activity level
def calculateCaloriesByActivity(check_activitylevel, x, y, mainCharacterBMR):
    if check_activitylevel == str(x):
        mainCharacterBMRWithActivity = float(mainCharacterBMR) * y
        return calculateCaloriesByGoal(MainCharacter.get_goal(MainCharacter), mainCharacterBMRWithActivity)
    else:
        x = x + 1
        y = y + 0.10
        return calculateCaloriesByActivity(check_activitylevel, x, y, mainCharacterBMR)

# this function is the last function to calculate the daily calorie need of the user
# it receives the calories with activity through the parameter
# checks what the user filled in as goal and then goes into that particular statement
# at the end of each condition the calories will be set for the maincharacter object
def calculateCaloriesByGoal(check_goal, mainCharacterBMRWithActivity):
    if check_goal == 'gain weight':
        mainCharacterTotalCalories = float(mainCharacterBMRWithActivity) + 300
        MainCharacter.set_dailycalories(MainCharacter, mainCharacterTotalCalories)
    if check_goal == 'lose weight':
        mainCharacterTotalCalories = float(mainCharacterBMRWithActivity) - 300
        MainCharacter.set_dailycalories(MainCharacter, mainCharacterTotalCalories)
    if check_goal == 'stay at weight':
        mainCharacterTotalCalories = mainCharacterBMRWithActivity
        MainCharacter.set_dailycalories(MainCharacter, mainCharacterTotalCalories)
    faketype("Your daily calorie need is " + str("{:.0f}".format(MainCharacter.get_dailycalories(MainCharacter))) + " kcal\n\n\n\n")
    return endOfUserRegistration()

# this function show the end dialog of getting information from the user
def endOfUserRegistration():
    faketype("Thank you for providing us with your information\n")

    faketype("You will now enter the real game\n")

    faketype("Here you will start with 5 random meals\n"
          "You can use the number 0 to 4 to choose one of the meals\n"
          "After chosing a meal you will get recommendations based on your selected meal\n"
          "While playing you will earn points which you can buy items with\n"
          "You can play as long as you like and choose as many meals as you like\n"
          "Goodluck in the darkness!\n\n\n")
