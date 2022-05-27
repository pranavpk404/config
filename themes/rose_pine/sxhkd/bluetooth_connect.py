from os import system


system("bluetoothctl power on")
system("bluetoothctl remove 11:11:22:AC:8D:70")
system("bash /home/pranav/.config/sxhkd/bluetooth_connect.sh -s 5")
system("bash /home/pranav/.config/sxhkd/bluetooth_connect.sh -c 11:11:22:AC:8D:70")
