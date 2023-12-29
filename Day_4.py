'''Problem Statement :
time based greetings script run the script  run the script to get personalized greeting -good morning,good afternoon ,good nightbased on the current time'''

#solution
import datetime

def get_greeting():
    current_time = datetime.datetime.now().time()

    if 5 <= current_time.hour < 12:
        return "Good morning!"
    elif 12 <= current_time.hour < 17:
        return "Good afternoon!"
    elif 17 <= current_time.hour <19:
        return "Good evening!"
    else:
        return "Good night!"


greeting = get_greeting()
print(greeting)
