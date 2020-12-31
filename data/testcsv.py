import csv
import datetime
import subprocess
import time
import os


# with open("output.csv","r") as f:
#     read=csv.reader(f)
#     for i in read:
#         if "Voltage" in i[0]:
#             i[0] = "Output_Voltage"
#         print(i)

def command(cmd):
    if cmd == 'START':
        try:
            os.remove("outputAvg.csv")
        except:
            pass
    with open("command.csv", "w") as f:
        write = csv.writer(f)
        write.writerow([cmd])


# with open("command.csv", "w") as f:
#     write = csv.writer(f)
#     write.writerow(["START"])

def start():
    command("END")
    subprocess.Popen(
        '"C:/Users/TenXer_Admin/AppData/Local/UiPath/app-20.10.2/UiRobot.exe" -file "D:/RE01/uipath/RNS-RE01/avg.xaml"')
    print("started uipath")
    time.sleep(5)
    for i in range(20):
        command("START")
        print("START")
        time.sleep(8)

        command("END")
        print("END")
        time.sleep(3)

    time.sleep(10)
    command("EXIT")
    # time.sleep(3)
    # with open("D:/RE01/uipath/RNS-RE01/data/outputAvg.csv", "r") as f:
    #     read = csv.reader(f)
    #     for i in read:
    #         print(i)

    # print("collected 1st avg data")
    # time.sleep(5)
    #
    # command("START")
    # print("START for 2nd time")
    # time.sleep(6)
    #
    # command("END")
    # print("END")
    # time.sleep(3)
    # with open("D:/RE01/uipath/RNS-RE01/data/outputAvg.csv", "r") as f:
    #     read = csv.reader(f)
    #     for i in read:
    #         print(i)
    # print("collected 2nd avg data")
    # command("ULP")


# start()
while True:
    command("START")
    time.sleep(20)
    command("END")
    time.sleep(3)
# time.sleep(15)
# command("EXIT")
# subprocess.Popen(
#         '"C:/Users/TenXer_Admin/AppData/Local/UiPath/app-20.10.2/UiRobot.exe" -file "D:/RE01/uipath/RNS-RE01/STM32_APP.xaml"')
# time.sleep(5)
# command("MODE")
# time.sleep(5)
# command("EXIT")
# time.sleep(5)
# command("EXIT")
# subprocess.Popen('"C:/Users/TenXer_Admin/AppData/Local/UiPath/app-20.10.2/UiRobot.exe" -file "D:/RE01/uipath/RNS-RE01/avg.xaml"')
#
# command("EXIT")
# time.sleep(15)
# command("EXIT")
# command("START") subprocess.Popen('"C:/Users/TenXer_Admin/AppData/Local/UiPath/app-20.10.2/UiRobot.exe" -file
# "D:/RE01/uipath/RNS-RE01/avg.xaml"') time.sleep(5) command("STOP") # subprocess.Popen(
# '"C:/Users/TenXer_Admin/AppData/Local/UiPath/app-20.10.2/UiRobot.exe" -file "D:/RE01/uipath/RNS-RE01/avg.xaml"')
# time.sleep(20) command("END") command("")


# subprocess.Popen('"C:/Users/TenXer_Admin/AppData/Local/UiPath/app-20.10.2/UiRobot.exe" -file
# "D:/RE01/uipath/RNS-RE01/avg.xaml"') with open("outputAvg.csv","r") as f: read=csv.reader(f) for i in read: print(i)


# ms = 1607496813180.54
# base_datetime = datetime.datetime( 1970, 1, 1 )
# delta = datetime.timedelta( 0, 0, 0,ms )
# target_date = base_datetime + delta
# print(target_date)
