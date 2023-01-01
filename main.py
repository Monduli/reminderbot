from win10toast import ToastNotifier
from datetime import datetime
import random
import time

def sleep():
    time.sleep(1)

def check_in(time_set):
    tasks = []
    while True:
        min = datetime.now().minute
        if min == 0 or (min == 30 and time_set == "half"):
            toast = ToastNotifier()
            toast.show_toast(
                "It's been an hour!",
                "Time to check in with ReminderBot.",
                icon_path = "./icon.ico",
                duration = 10,
                threaded = True
            )
            word = ""
            while word != "Okay":
                print("Drink some water. (Type 'Okay' when complete.)")
                word = input()
                if word == "q":
                    return tasks
                elif word != "Okay":
                    print("You didn't confirm that you drank water!")
                    sleep()
                else:
                    print("Good job.")
                    sleep()
            print("Are you focusing on work? (Yes or No)")
            word = input()
            if word == "q":
                return tasks
            elif word == "No":
                print("Try to focus. Close all games or distracting applications.")
                sleep()
                r = random.randint(0, 5)
                colors_list = ["Red", "Yellow", "Purple", "Blue", "Green", "Orange"]
                color = colors_list[r]
                print("Ground yourself by finding 5 objects around the room that are " + color + ".")
                sleep()
                print("Think about what you can hear and feel.")
                sleep()
                print("Did you complete this grounding exercise?")
                word = input()
                if word == "Yes":
                    print("Good. Try to focus better next time!")
                    sleep()
                else:
                    print("You need to do this exercise and regain your focus.")
                    sleep()
            elif word == "Yes":
                print("Good to hear!")
                sleep()
            else:
                print("That is not a word nor is it an answer to my question, probably.")
            print("What did you complete during this time frame?")
            task = input()
            if tasks == []:
                print("This is the first task you've completed today.")
                sleep()
            else:
                print("During the last check-in, you said that you: " + tasks[len(tasks)-1])
                sleep()
            tasks.append(task)
            number, numtwo = 7, 7
            while number == numtwo:
                number = random.randint(0, 5)
                numtwo = random.randint(0, 5)
            affirmations = [
                "Remember, you are smart enough to become something great.",
                "Remember that there are people counting on you that love you very much and only want you to succeed and be happy.",
                "Remember that drinking water will keep you from being grumpy and feeling bad later.",
                "Remember that everything starts from somewhere. You'll feel better once you start scaling the mountain.",
                "Remember to keep something happy in your space so you can remember life is about having fun.",
                "Remember that you made this bot to keep yourself in check. It is here to help you!"
            ]
            print(affirmations[number])
            sleep()
            print(affirmations[numtwo])
            sleep()
            print("That's all for now. Check in with you again in a while!")
            sleep()
            print("Waiting...")
        else:
            time.sleep(60)

def welcome():
    print("WELCOME TO DAN'S REMINDERBOT v 0.1!")
    sleep()
    print("You will receive a reminder every hour to complete several tasks.")
    sleep()
    print("Would you like reminders every half hour or hour? (Type 'half' or 'hour'.)")
    sleep()
    time_set = input()
    if time_set == "half":
        print("Okay! See you back here at the next half hour!")
        sleep()
    if time_set == "hour":
        print("Okay! See you back here at the next hour!")
        sleep()
    now = datetime.now()
    print("Waiting...")
    tasks = check_in(time_set)
    then = datetime.now()
    elapsed = then - now
    print("Session complete. Your session lasted " + str(elapsed) + " minutes.")
    sleep()
    print("Here are the tasks you completed during this session:")
    sleep()
    for element in tasks:
        print(element)
        sleep()
    print("Thank you for using my ReminderBot. See you next time! (Press enter to exit.)")
    exit = input()
    quit()


if __name__ == "__main__":
    welcome()