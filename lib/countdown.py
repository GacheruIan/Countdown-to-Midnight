# your code goes here!

import time

def countdown(number):
    while number >= 1:
        print(f"{number} SECONDS(S)!")
        countdown_with_sleep()
        number -= 1
    print("HAPPY NEW YEAR!")



def countdown_with_sleep():
    time.sleep(1)



# countdown_with_sleep()
countdown(5)



