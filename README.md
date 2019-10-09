# Laptop Battery Notifier Program

**Description:** This Program monitors the Laptop Battery Percentage and notifies for Low Battery or Full Battery Charge with an alarm sound.

**Supported OS:** Ubuntu/Linux Mint/Windows 10

**Python Version:** Python 3.6

**Requirements:**

*Linux:*

```shell
sudo apt-get install python3-tk
```

Other required python packages are listed on requirements.txt

```shell
sudo pip3 install -r requirements.txt
```
*Windows:*

```shell
pip install -r requirements.txt
```

**To Run the Program:**

*Linux:*

```shell
python3 tkinter_battery_notifier.py
```
*Windows:*

```shell
python tkinter_battery_notifier.py
```

**GUI Contents:**

1. Battery Percentage
2. Charge Status

**GUI options:**  

1. Check/UnCheck Low Battery Notification (Notifies when Battery is Less than 20 Percentage).
2. Check/UnCheck Full Battery Notification (Notifies when Battery is More than 99 Percentage).
3. Change Alarm music.

**Notes:**  

1. The Program has been tested on Ubuntu 18.04, Linux Mint 19 and Windows 10.
2. The Program also works on the laptop with multiple batteries. The charge of multiple batteries are combined together for processing.
3. The Program should also work on all Python3 Versions.