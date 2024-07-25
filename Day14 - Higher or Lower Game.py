import Day14_HelperFile
import random


def getUser():
    """
    Get a random instagram user and their followers count.
    :return: User and follower count of user.
    """
    user, followers = random.choice(list(Day14_HelperFile.instagram_followers.items()))
    return user, followers


def addCommas(number):
    return "{:,}".format(number)


score = 0
isOver = False
currentUser = getUser()
while not isOver:
    nextUser = getUser()
    guess = (
        input(f"{currentUser[0]} - {addCommas(currentUser[1])} followers vs {nextUser[0]}.\nHow does {currentUser[0]}"
              f"'s followers count compare to {nextUser[0]}'s? Type 'higher', 'lower', or 'equal'.\nYour Guess: ")
        .strip().lower())
    if guess == 'higher' and currentUser[1] > nextUser[1]:
        score += 1
        print(f"\nCorrect! {currentUser} has a higher follower count than {nextUser}.")
        currentUser = nextUser
    elif guess == 'lower' and currentUser[1] < nextUser[1]:
        score += 1
        print(f"\nCorrect! {currentUser} has a lower follower count than {nextUser}.")
        currentUser = nextUser
    elif guess == 'equal' and currentUser[1] == nextUser[1]:
        score += 1
        print(f"\nCorrect! {currentUser} has a lower follower count than {nextUser}.")
        currentUser = nextUser
    else:
        isOver = True
        print(
            f"Incorrect! {currentUser[0]} has {addCommas(currentUser[1])} followers and {nextUser[0]} has"
            f" {addCommas(nextUser[1])}.")
