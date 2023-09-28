import time
from termcolor import colored
import asyncio
import sys
import simpleobsws
import random

ws = simpleobsws.WebSocketClient(
    url="ws://localhost:4455",
    password="your_password",
)


async def switch_scene(scene_name):
    await ws.connect()
    await ws.wait_until_identified()
    data = {"sceneName": scene_name}
    request = simpleobsws.Request("SetCurrentProgramScene", data)
    ret = await ws.call(request)
    if ret.ok():
        print(
            colored("Переключаемся на другую сцену: ", "light_magenta"),
            colored(f"{scene_name}", "green"),
        )


def loading_animation(duration):
    animation = [
        "[■□□□□□□□□□]",
        "[■■□□□□□□□□]",
        "[■■■□□□□□□□]",
        "[■■■■□□□□□□]",
        "[■■■■■□□□□□]",
        "[■■■■■■□□□□]",
        "[■■■■■■■□□□]",
        "[■■■■■■■■□□]",
        "[■■■■■■■■■□]",
        "[■■■■■■■■■■]",
    ]
    for i in range(duration):
        time.sleep(1)
        sys.stdout.write("\r" + animation[i % len(animation)])
        sys.stdout.flush()
    print()


class State:
    def __init__(self, name):
        self.name = name
        self.transitions = []

    async def update(self):
        print(colored("Текущее состояние: ", "red"), colored(f"{self.name}", "green"))
        loading_animation(10)
        await asyncio.sleep(1)

    async def set_scene(self, scene_name):
        if scene_name != self.name:
            await switch_scene(scene_name)
            self.name = scene_name


class PresentationState(State):
    async def update(self):
        await super().update()
        print(
            colored("Обновление для состояния ", "blue"),
            colored(f"{self.name}", "green"),
        )
        new_scene = random.choice(["Аудитория", "Спикер"])
        await self.set_scene(new_scene)
        self.name = new_scene  # Update the state name


class AuditoryState(State):
    async def update(self):
        await super().update()
        print(
            colored("Обновление для состояния ", "blue"),
            colored(f"{self.name}", "green"),
        )
        new_scene = random.choice(["Презентация", "Спикер"])
        await self.set_scene(new_scene)
        self.name = new_scene


class SpeakerState(State):
    async def update(self):
        await super().update()
        print(
            colored("Обновление для состояния ", "blue"),
            colored(f"{self.name}", "green"),
        )
        new_scene = random.choice(["Презентация", "Аудитория"])
        await self.set_scene(new_scene)
        self.name = new_scene
