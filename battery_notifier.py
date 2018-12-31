#!/usr/bin/python3

# Version - 1.0
# Date - 31/Dec/2018
# This Program works with Battery Sensors and gets the Battery charge details.
# It also plays alarm to notify low or full battery.

# Sample file downloaded from the below link:
# http://file-examples.com/wp-content/uploads/2017/11/file_example_MP3_700KB.mp3

__Author__ = "Rajesh Kumar N"
__version__ = "0.1"

import json
from playsound import playsound, PlaysoundException
import psutil
import os
from time import sleep

class BatteryNotifier:
    current_dir = os.path.dirname(os.path.abspath(__file__))

    def __init__(self):
        self.battery = psutil.sensors_battery()

        self.low_battery_flag = True
        self.__low_value = 20

        self.full_charge_flag = True
        self.__full_value = 99

        self.alarm_json_file = os.path.join(self.current_dir, "alarm_file.json")
        self.get_alarm_file_path()

    def get_alarm_file_path(self):
        with open(self.alarm_json_file) as alarm_file:
            self.alarm_file = json.load(alarm_file)

    def set_alarm_file_path(self, file_path):
        if os.path.exists(file_path):
            with open(self.alarm_json_file, 'w') as alarm_out_file:  
                json.dump(file_path, alarm_out_file)

        with open(self.alarm_json_file) as alarm_file:
            self.alarm_file = json.load(alarm_file)

    def is_power_plugged(self):
        try:
            return self.battery.power_plugged
        except AttributeError:
            print("Kindly Retry again...")
    
    def get_battery_percentage(self):
        return self.battery.percent

    def set_low_battery_flag(self):
        if not self.low_battery_flag:
            self.low_battery_flag = True
        else:
            self.low_battery_flag = False

    def get_low_battery_flag(self):
        return self.low_battery_flag

    @property
    def low_value(self):
        return self.__low_value
    
    @low_value.setter
    def low_value(self, value):
        self.__low_value = value

    def low_battery_notification(self):
        if not self.is_power_plugged() and self.get_battery_percentage() <= self.low_value:
            try:
                playsound(self.alarm_file)
            except PlaysoundException:
                print("Exception occurred while playing %s" % self.alarm_file)

    def set_full_charge_flag(self):
        if not self.full_charge_flag:
            self.full_charge_flag = True
        else:
            self.full_charge_flag = False

    def get_full_charge_flag(self):
        return self.full_charge_flag

    @property
    def full_value(self):
        return self.__full_value

    def full_charge_notification(self):
        if self.is_power_plugged() and self.get_battery_percentage() >= self.full_value:
            try:
                playsound(self.alarm_file)
            except PlaysoundException:
                print("Exception occurred while playing %s" % self.alarm_file)

    def change_alarm_file(self, new_file_path):
        if os.path.exists(new_file_path):
            self.alarm_file = new_file_path
        else:
            raise FileNotFoundError

if __name__ == "__main__":

    while True:
        notifier_obj = BatteryNotifier()
        print("Current Battery Percentage: %s" % notifier_obj.get_battery_percentage())
        notifier_obj.low_battery_notification()
    
        notifier_obj.full_charge_notification()

        sleep(60)