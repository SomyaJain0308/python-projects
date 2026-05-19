
"""
The Basic Idea:
Time Management: The project demonstrates how to handle time-based inputs (minutes and seconds) from a user to create a countdown timer.
Logic Flow: The program uses a loop that updates the remaining time, displaying it to the user as it counts down to zero.
Utility Implementation: It shows how to integrate external assets, such as royalty-free sound effects, to trigger an alert once the timer reaches zero.
"""
from time import sleep

def get_time():
    while True:
        try:
            hours = int(input("Hours: "))
            minutes = int(input("Minutes: "))
            seconds = int(input("Seconds: "))
            if hours < 0 or minutes < 0 or seconds < 0:
                print("Type a positive number dumbass")
                continue
            else:
                return hours*3600 + minutes*60 + seconds
        except ValueError:
            print("Type a number dumbass")

def countdown(secs):
    sleep(secs)
    playsound('alarm.mp3')
    print("Time's up!")

def main():
    countdown(get_time())

if __name__=="__main__":
    main()