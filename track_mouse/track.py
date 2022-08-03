from pynput.mouse import Listener
import logging

logging.basicConfig(filename="mouse_log.txt", level=logging.DEBUG, format='%(asctime)s: %(message)s')

def on_move(x, y):
    #logging.info(f'Mouse Moved to ({x}, {y})')
    pass

def on_click(x, y, button, pressed):
    if pressed:
        logging.info(f'Mouse clicked at ({x}, {y}), with {button}')

def on_scroll(x, y, dx, dy):
    #logging.info('Mouse Scrolled at ({x}, {y})({dx}, {dy})')
    pass

with Listener(on_move=on_move, on_click=on_click, on_scroll=on_scroll) as listener:
    listener.join()

