import sys
from auth import MiBand3
from cursesmenu import *
from cursesmenu.items import *
from constants import ALERT_TYPES
import time
import os

def call_immediate():
    print('Sending Call Alert')
    time.sleep(1)
    band.send_alert(ALERT_TYPES.PHONE)
def msg_immediate():
    print('Sending Message Alert')
    time.sleep(1)
    band.send_alert(ALERT_TYPES.MESSAGE)
def detail_info():
    print('MiBand')
    print('Soft revision:',band.get_revision())
    print('Hardware revision:',band.get_hrdw_revision())
    print('Serial:',band.get_serial())
    print('Battery:', band.get_battery_info())
    print('Time:', band.get_current_time())
    print('Steps:', band.get_steps())
    raw_input('Press Enter to continue')
def custom_message():
    band.send_custom_alert(5)

def custom_call():
    # custom_call
    band.send_custom_alert(3)

def custom_missed_call():
    band.send_custom_alert(4)

def l(x):
    print('Realtime heart BPM:', x)

def heart_beat():
    band.start_raw_data_realtime(heart_measure_callback=l)
    raw_input('Press Enter to continue')

def change_date():
    band.change_date()

def updateFirmware():
    fileName = raw_input('Enter the file Name with Extension\n')
    band.dfuUpdate(fileName)

MAC_ADDR = sys.argv[1]
print('Attempting to connect to ', MAC_ADDR)
band = MiBand3(MAC_ADDR, debug=True)
band.setSecurityLevel(level = "medium")

# Authenticate the MiBand
if len(sys.argv) > 2:
    if band.initialize():
        print("Initialized...")
    band.disconnect()
    sys.exit(0)
else:
    band.authenticate()

def append_function_item(menu, text, fn):
  menu.append_item(FunctionItem(text, fn))

menu = CursesMenu("MiBand MAC: " + MAC_ADDR, "Select an option")
append_function_item(menu, "View Band Detail info", detail_info)
append_function_item(menu, "Send a High Prority Call Notification", call_immediate)
append_function_item(menu, "Send a Medium Prority Message Notification", msg_immediate)
append_function_item(menu, "Send a Message Notification", custom_message)
append_function_item(menu, "Send a Call Notification", custom_call)
append_function_item(menu, "Send a Missed Call Notification", custom_missed_call)
append_function_item(menu, "Change Date and Time", change_date)
append_function_item(menu, "Get Heart BPM", heart_beat)
append_function_item(menu, "DFU Update", updateFirmware)
menu.show()
