import datetime, os, time

def cls():
    os.system('clear')

def clock():
    while True:
        hour = datetime.datetime.now().hour
        minute = datetime.datetime.now().minute
        second = datetime.datetime.now().second
        day = ""

        if hour >= 13 and (hour <= 23 and minute <= 59 and second <= 59):
            day = "pm"
        else:
            day = "am"

        print("Time now: {}:{}:{} {}".format(hour, minute, second, day))
        time.sleep(0.99)
        cls()

if __name__ == "__main__":
    clock()