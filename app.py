import pymem
import pymem.process
import keyboard
import time

dwLocalPlayer = 0xC3F6C0
dwForceJump = 0xC6E460

hotkey = str(input("Hotkey: "))


pm = pymem.Pymem("hl2.exe")
client = pymem.process.module_from_name(pm.process_handle, "client.dll").lpBaseOfDll

while True:
    if keyboard.is_pressed("escape"):
        exit()

    if keyboard.is_pressed(hotkey):
        force_jump = client+dwForceJump
        player = pm.read_int(client+dwLocalPlayer)
        pm.write_int(force_jump, 6)
        time.sleep(0.05)
        pm.write_int(force_jump, 6)
        time.sleep(0.05)
