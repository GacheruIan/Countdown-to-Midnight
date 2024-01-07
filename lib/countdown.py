# your code goes here!

import time

def countdown(num = 10):
    while num >= 1:
        print(f"{num} SECOND(S)!")
        num -= 1
    print("HAPPY NEW YEAR!")


def countdown_with_sleep(number = 5):
    while number >= 1:
        print(f"{number} SECOND(S)!")
        number -= 1
        time.sleep(1)
    print("HAPPY NEW YEAR!")

countdown() 
countdown_with_sleep()   













