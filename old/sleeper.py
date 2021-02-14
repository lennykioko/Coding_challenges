import time

def sleeper():
    try:
        sleep_time = input("Enter time to sleep in seconds: ")
        sleep_time = float(sleep_time)
        print("Initialized at {}".format(time.ctime()))
        time.sleep(sleep_time)
        print("Started executing after-block at {}".format(time.ctime()))
        # enter code you want to execute after the sleep time here

    except EOFError:
        print("You need to enter a number ")
    except ValueError:
        print("Please enter a valid number ")

try:
    sleeper()
except KeyboardInterrupt:
    print("KeyboardInterrupt received: Exiting.....")
    exit()
    