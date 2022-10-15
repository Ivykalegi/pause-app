import math
import time


print("To start a timer, you need to select the amount of time you want to study from the following options")
print("A. 20 mins")
print("B. 25 mins")
print("C. 30 mins")
study_time_in_min = int(input("Select the amount of time you want to study:"))

break_time_in_min = int(input("How long would you like your break to be ? 5 , 10 or 15 min?"))

target_time_in_hours = int(input("Select target study time for the day in hours?"))

def count_down(t):
    """ Function to count down seconds to zero """
    while t > 0:
        t -= 1
        time.sleep(1)
        if t == 0:
            break
        elif t < 10:
            print(f"0{t}")
        elif 10 <= t < 60:
            print(f"{t}")
        else:
            count_in_min = math.floor(t / 60)
            count_in_sec = t % 60
            if count_in_sec < 10:
                print(f"{count_in_min}:0{count_in_sec}")
            else:
                print(f"{count_in_min}:{count_in_sec}")



def check_target_time(target_time_in_hours):
    """
    Function to keep track of the target study time  and
    check whether it has been reached
    assume target time is received in hours
    """

    total_no_of_study_time = (target_time_in_hours * 60) // study_time_in_min
    return total_no_of_study_time


def break_timer():
    break_time_in_sec = break_time_in_min * 60
    print("Your break time starts now")
    count_down(break_time_in_sec)


def study_timer():
    study_time_in_seconds = study_time_in_min * 60
    print("You study time  starts now")
    count_down(study_time_in_seconds)


if __name__ == "__main__":
    target = check_target_time(target_time_in_hours)
    while target > 0:
        study_timer()
        break_timer()
        target -= 1

    print("Your study time has finished")



