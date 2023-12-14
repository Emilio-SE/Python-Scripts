'''--------------------------
Author: Emilio Sánchez Enríquez.
Created: September 4, 2022
Last modified: March 26, 2023 By Emilio Sánchez Enríquez.
--------------------------'''

#Description:
#Throws a message when battery is above 80% and it's plugged in. Also, when is below 25% and it's unplugged.

from psutil import sensors_battery                      #Requires to install this library: 'pip install psutil'
from time import sleep
import win32con                                         # Requires to install this library: 'pip install pywin32'
from win32gui import GetForegroundWindow, ShowWindow    #
from win10toast import ToastNotifier                    #Requires to install this library: 'pip install win10toast'

#hwnd = GetForegroundWindow()
#ShowWindow(hwnd, win32con.SW_HIDE)                      #To hide cmd.

def launch_notification(title_msg, description_msg):
    toaster = ToastNotifier()
    toaster.show_toast(
        title_msg,
        description_msg,
        duration=10
    )
    
show_unplug_charger_urg_msg = True
show_unplug_charger_msg = True
show_plug_in_charger_msg = True

while(True):

    battery = sensors_battery()
    is_plugged = battery.power_plugged
    percent_battery = battery.percent
    
    if is_plugged:
        show_plug_in_charger_msg = True
    else:
        show_unplug_charger_msg = True
        show_unplug_charger_urg_msg = True

    print(show_plug_in_charger_msg , show_unplug_charger_msg, show_unplug_charger_urg_msg)

    if (percent_battery >= 25 and is_plugged) and show_unplug_charger_msg:
        launch_notification("Battery Sufficiently Charged", str(percent_battery) + "% Battery. Unplug the charger." )
        print("Battery Sufficiently Charged", str(percent_battery) + "% Battery. Unplug the charger.")
        show_unplug_charger_msg = False

    elif (percent_battery >= 90 and is_plugged) and show_unplug_charger_urg_msg:
        launch_notification("Battery Charged", str(percent_battery) + "% Battery. Please, unplug the charger." )
        print("Battery Charged", str(percent_battery) + "% Battery. Please, unplug the charger.")
        show_unplug_charger_urg_msg = False

    elif (percent_battery <= 25 and (not is_plugged) ) and show_plug_in_charger_msg:
        launch_notification("Low Battery", str(percent_battery) + "% Battery. Plug in the charger." )
        print("Low Battery", str(percent_battery) + "% Battery. Plug in the charger.")
        show_plug_in_charger_msg = False
    
    sleep(1)
