class StateMachine:
    def __init__(self, initial_state):
        self.current_state = initial_state

    def run(self):
        while True:
            self.current_state.update()
            for transition in self.current_state.transitions:
                if transition.needTransit():
                    self.current_state = transition.next_state
