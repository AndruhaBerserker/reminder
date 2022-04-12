from tkinter import *
import time
from playsound import playsound


def main(set_time):
    while True:
        time.sleep(set_time)
        playsound('beep.wav')
        notify = Label(clock,
                       text="Do an exercises and push the button",
                       bg="black", fg="red",
                       font=("Arial", 10, "bold")).place(x=50, y=80)
        time.sleep(2)
        break


# Timer for 30 min(1800 sec)
def actual30():
    set_time = 1800
    main(set_time)


# Timer for 60 min(3600 sec)
def actual60():
    set_time = 3600
    main(set_time)


# GUI
clock = Tk()
clock.title("Reminder")
clock.geometry("300x120")
hour_time= Button(clock, text ="30 min",fg="red",width =10,command = actual30).place(x=50,y=30)
min_time = Button(clock, text="60 min", fg="red", width=10, command= actual60).place(x=150, y=30)
clock.mainloop()
