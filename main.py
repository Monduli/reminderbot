from win10toast import ToastNotifier
from datetime import datetime, timedelta
import random
import time
import sys
import os

def sleep():
    time.sleep(1)

def check_in(time_set, start, mode):
    
    tasks = []
    while True:
        minute = datetime.now().minute
        sys.stdout.flush()
        elapsed = round(time.time() - start, 2)
        if time_set == "15":
            if minute == 0:
                time_left = 0
            elif minute < 16:
                time_left = 15 - minute
            elif minute < 31:
                time_left = 30 - minute
            elif minute < 46:
                time_left = 45 - minute
            else:
                time_left = 60 - minute               
        elif time_set == "30":
            x = 60 - minute
            if minute < 31 and minute > 0:
                time_left = 30 - minute
            elif x == 60:
                time_left = 0
            else:
                time_left = 60 - minute
        elif time_set == "60":
            x = 60 - minute
            if x == 60:
                time_left = 0
            else:
                time_left = 60 - minute
        print("\rWaiting... (Time elapsed: " + str(timedelta(seconds=round(elapsed))) + ". Time until next check-in: " + str(time_left) + ")", end='')
        if time_left == 0 or minute == 0:
            toast = ToastNotifier()
            path = "icon.ico"
            os.chdir('C:/Programming/reminderbot')
            toast.show_toast(
                "It's been a while!",
                "Time to check in with ReminderBot.",
                icon_path = path,
                duration = 10,
                threaded = True
            )
            word = ""
            while word != "Okay":
                begin = time.time()
                print("\nDrink some water. (Type 'Okay' when complete.)")
                word = input()
                if word == "q":
                    return tasks
                elif word != "Okay":
                    print("You didn't confirm that you drank water!")
                    sleep()
                else:
                    print("Good job.")
                    sleep()
                time_taken = round(time.time() - start, 2)
                print("It took you " + time_taken + " to respond.")
                sleep()
            if mode != 1:
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
                    "Remember that you made this bot to keep yourself in check. It is here to help you!",
                    "Remember to do your laundry on time. There's not really a bad time to do laundry.",
                    "Remember to clean all the dirty dishes off of your desk. Dirty desk is a dirty mind (not like that).",
                    "Remember to clean your work room. It can be distracting if it isn't in good condition."
                ]
                print(affirmations[number])
                sleep()
                print(affirmations[numtwo])
                sleep()
            print("That's all for now. Check in with you again in a while!")
            sleep()
            print("Please wait 60 seconds for reminderbot to resume counter.")
            time.sleep(60)
        else:
            time.sleep(1)

def welcome():
    start = time.time()
    print("WELCOME TO DAN'S REMINDERBOT v 0.1!")
    sleep()
    print("You will receive a reminder every hour to complete several tasks.")
    sleep()
    ahead = 0
    while ahead != 1:
        print("Please select a mode. (1 - Study Mode, 2 - Play Mode)")
        mode = input()
        if mode != "1" and mode != "2":
            print("Please enter a 1 or a 2.")
        else:
            ahead = 1
    sleep()
    ahead = 0
    while ahead != 1:
        print("Would you like reminders every 15, 30, or 60 minutes? (Type '15', '30' or '60'. Type 'q' to quit.)")
        sleep()
        time_set = input()
        if time_set == "15":
            print("Okay! See you in 15 minutes or so!")
            sleep()
            ahead = 1
        elif time_set == "30":
            print("Okay! See you back here at the next half hour!")
            sleep()
            ahead = 1
        elif time_set == "60":
            print("Okay! See you back here at the next hour!")
            sleep()
            ahead = 1
        elif time_set == "q":
            print("Goodbye!")
            return
        else:
            print("You did not enter a valid time.")
            sleep()
    now = datetime.now()
    print("Waiting...", end='')
    tasks = check_in(time_set, start, mode)
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