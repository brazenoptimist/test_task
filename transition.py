import random


class Transition:
    def __init__(self, next_state):
        self.next_state = next_state

    def needTransit(self):
        pass  # Абстрактный метод, будет реализован в подклассах


class TimeTransition(Transition):
    probability = 0.1

    def needTransit(self):
        return random.random() < self.probability


class PresentationTransition(Transition):
    probability = 0.1

    def needTransit(self):
        return random.random() < self.probability
