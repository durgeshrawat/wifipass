import subprocess
wifinames=subprocess.check_output("netsh wlan show profiles", shell=True, universal_newlines=True)
print(wifinames)
targetwifi=input("Target WiFi: ")
info=subprocess.check_output(f"netsh wlan show profile {targetwifi} key=clear", shell=True, universal_newlines=True)
password=info.split('\n')[32].split(':')[1]
print('PASWORD :',password)
