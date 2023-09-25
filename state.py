# state.py

import time
from termcolor import colored


class State:
    def __init__(self, name):
        self.name = name
        self.transitions = []

    def update(self):
        print(f"Текущее состояние:", colored(self.name, "magenta"))
        time.sleep(1)


class PresentationState(State):
    COLOR = "\033[93m"  # Yellow text color
    RESET = "\033[0m"  # Reset text color

    def update(self):
        super().update()
        print(colored("Обновление для состояния Презентация", "red"))


class AuditoryState(State):
    def update(self):
        super().update()
        print(colored("Обновление для состояния Аудитория", "green"))


class SpeakerState(State):
    def update(self):
        super().update()
        print(colored("Обновление для состояния Спикер", "blue"))
