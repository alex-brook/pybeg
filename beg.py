#!/usr/bin/env python3

import time
import random
import pyautogui as gui

BEG_MSG = "pls beg"
SEARCH_MSG = "pls search"
GIVE_MSG = "pls give 100 alex#2592"
SELL_CHILL_PILL_MSG = "pls sell chilpill"
SELL_BREAD_MSG = "pls sell bread"
SELL_COOKIE_MSG = "pls sell cookie"

def random_typing_interval():
    return random.uniform(0.1, 0.5)

def random_extra_wait():
    return random.randint(0,5)

def random_string():
    res = ""
    length = random.randint(1,20)
    for i in range(0, length):
        c = chr(ord('A') + random.randint(0,26))
        res += c
    return res

def say(msg):
    gui.typewrite(msg, random_typing_interval())
    gui.press("enter")


print("starting in 5 seconds...")
time.sleep(5)

i = 0
while True:
    print(f"beg iteration {i}.")
    start_time = time.time()
    say(random_string())
    say(BEG_MSG)
    say(SEARCH_MSG)
    say(GIVE_MSG)
    print("waiting")
    time.sleep(60 + random_extra_wait())
    i = i + 1
