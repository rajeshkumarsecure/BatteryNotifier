#!/usr/bin/python3

# Version - 1.0
# Date - 31/Dec/2018
# This Program provides GUI for Battery Notifier.
# It provide options for Modifying settings.

__Author__ = "Rajesh Kumar N"
__version__ = "0.1"

import sys
sys.path.append('../')

from functools import partial
from multiprocessing import Process
from tkinter import *
from tkinter import filedialog
from time import sleep

from batterynotifier.battery_notifier import BatteryNotifier


def browse_func(battery_notifier_obj):    
    filename = filedialog.askopenfilename(initialdir="/", title="Select a Music/Sound file", filetypes = [("Audio files", "*.3gp *.aa *.aac *.aax *.act *.aiff *.amr *.ape *.au *.awb *.dct *.dss *.dvf *.flac *.gsm *.iklax *.ivs *.m4a *.m4b *.m4p *.mmf *.mp3 *.mpc *.msv *.nsf *.ogg *.oga *.mogg *.opus *.ra *.rm *.raw *.sln *.tta *.vox *.wav *.wma *.wv *.webm *.8svx",)])
    if filename:
        battery_notifier_obj.set_alarm_file_path(filename)


class TkinterGuiBatteryNotifier:

    def __init__(self):
        self.first_run = True
        self.process1 = None
        self.process2 = None
        self.root = Tk()

        self.var1 = None
        self.var2 = None

        self.battery_notifier_obj = None

        self.batt_value = None
        self.charge_status = None

    def create_elements_in_the_windows(self):
        self.battery_notifier_obj = BatteryNotifier()
        battery_perc = self.battery_notifier_obj.get_battery_percentage()
        battery_charge_status = self.battery_notifier_obj.is_power_plugged() 

        # Window title
        self.root.title('Battery Charge Notifier')

        Label(self.root, text='Battery Percentage').grid(row=0, sticky=W)
        self.batt_value = Label(self.root, text=str(battery_perc))
        self.batt_value.grid(row=0, column=1)

        Label(self.root, text='Battery Power Plugged').grid(row=2, sticky=W)
        self.charge_status = Label(self.root, text=str(battery_charge_status))
        self.charge_status.grid(row=2, column=1)

        Label(self.root, text="Notification Settings:").grid(row=4, sticky=W)

        self.var1 = IntVar(value=1)
        Checkbutton(self.root, text="Low Battery Notification", variable=self.var1).grid(row=5, sticky=W)

        self.var2 = IntVar(value=1)
        Checkbutton(self.root, text="Full Battery Notification", variable=self.var2).grid(row=6, sticky=W)

        browse_func_with_arg = partial(browse_func, self.battery_notifier_obj)
        Button(self.root, text="Browse", command=browse_func_with_arg).grid(row=8, sticky=W)

    def monitor_battery(self):
                
        self.battery_notifier_obj = BatteryNotifier()
        battery_perc = self.battery_notifier_obj.get_battery_percentage()
        battery_charge_status = self.battery_notifier_obj.is_power_plugged()

        self.batt_value["text"] = str(battery_perc)
        self.charge_status["text"] = str(battery_charge_status)

        if not self.first_run:
            if self.var1.get() == 1:
                if not self.process1 or not self.process1.is_alive():
                    self.process1 = Process(target=self.battery_notifier_obj.low_battery_notification)
                    self.process1.start()
                    # battery_notifier_obj.low_battery_notification()
            if self.var2.get() == 1:
                if not self.process2 or not self.process2.is_alive():
                    self.process2 = Process(target=self.battery_notifier_obj.full_charge_notification)
                    self.process2.start()
                    # battery_notifier_obj.full_charge_notification()
            self.root.after(1000, self.monitor_battery)
        else:
            self.first_run = False
            # After 1 second, update the status
            self.root.after(1000, self.monitor_battery)

    def mainloop_routine(self):
        # Launch the monitor battery program after 1 millisecond (when the window is loaded)
        self.root.after(1, self.monitor_battery)
        self.root.grid_columnconfigure(1, minsize=700)
        self.root.mainloop()


if __name__ == "__main__":
    gui_obj = TkinterGuiBatteryNotifier()
    gui_obj.create_elements_in_the_windows()
    gui_obj.mainloop_routine()