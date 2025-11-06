from pynput import mouse
import keyboard
import time

print("[*] Loaded all modules!")
side_button_pressed = False
print("[/] Moonwalk 0.1 python")
print("----SETUP----")
tim = float(input("Time pressing key: (enter 0 to default)"))
tim2 = float(input("Time delay key: (enter 0 to default)"))
if tim == 0.0:
    tim = 0.02
if tim2 == 0.0:
    tim2 = 0.03
button_def = input("[*] Button: (middle, x1, x2): ")
print(f'[*] Selected: {button_def}')
print(f"Time 1: {tim}")
print(f"Time 2: {tim2}")
def on_click(x, y, button, pressed):
    global side_button_pressed
    if button_def == "x1":
        if button == mouse.Button.x1:
            side_button_pressed = pressed
    if button_def == "x2":
        if button == mouse.Button.x2:
            side_button_pressed = pressed
    if button_def == "middle":
        if button == mouse.Button.middle:
            side_button_pressed = pressed

def perform_action():
    while True:
        if side_button_pressed:
            keyboard.press('A')
            time.sleep(tim)
            keyboard.release('a')

            keyboard.press('d')
            time.sleep(tim)
            keyboard.release('d')
   
            time.sleep(tim2)
        else:
            time.sleep(0.1)


listener = mouse.Listener(on_click=on_click)
listener.start()
perform_action()
