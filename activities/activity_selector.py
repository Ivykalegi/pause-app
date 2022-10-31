from guizero import *
from activity_manager import ActivityManager


# study timer functionality
def start_timer(window):
    timer_window = Window(window)
    timer_window.height = 100
    timer_window.width = 250

    current_time_left = 3

    timer_title = Text(timer_window, text="Study Pause Timer")

    timer = Text(timer_window, text="current time left")
    timer.repeat(60000, reduce_time())


def reduce_time():
    global timer
    if int(timer.value) > 0:
        timer.value = int(timer.value) - 1
    else:
        timer.value = "Times Up"


# activity functionality

def select_activities(value):
    ActivityManager = value

a = App()

t = Text(a, text="Choose your Pause Activity", color="black")

listbox = ListBox(
    a, 
    items=["Wellbeing", "Brain Gym"], 
    selected="black", 
    command=select_activities,
    scrollbar=True)

a.display()
a.enable()



def add_activity(choice):
    ActivityManager = choice
    select_activity = ActivityWidget(ActivityManager, activityBox)


class ActivityWidget(object):
    def __init__(self, descr, window):
        self.__widgetSpace = Box(window)
        self.__widgetDescr = Text(self.__widgetSpace, text=descr, align='left')
        self.__widgetDone = CheckBox(self.__widgetSpace, align='right')
        self.__widgetSpace.repeat(200, self.destroy_widget)

    def destroy_widget(self):
        try:
            if self.__widgetDone.value == 1:
                self.__widgetSpace.destroy()
        except:
            pass


app = App()

title = Text(app, text="Pause Study Break Activity")
pauseTimer = PushButton(app, text="Study Pause Timer", command=lambda: start_timer(app))
entryBox = Box(app)

activityBox = Box(app)

activityBox.width = 450
activityBox.height = 500
activityBox.bg = "white"

entryTxt = TextBox(entryBox, align="left")
entryTxt.width = 50

entryBtn = PushButton(entryBox, text="Add", command=lambda: add_activity(entryTxt.value), align="right")

app.display()
