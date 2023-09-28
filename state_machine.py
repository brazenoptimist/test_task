import asyncio


class StateMachine:
    def __init__(self, initial_state):
        self.current_state = initial_state

    def run(self):
        loop = asyncio.get_event_loop()
        loop.run_until_complete(self._async_run())

    async def _async_run(self):
        while True:
            await self.current_state.update()
            for transition in self.current_state.transitions:
                if transition.needTransit():
                    self.current_state = transition.next_state
