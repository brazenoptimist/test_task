from state import PresentationState, AuditoryState, SpeakerState
from transition import TimeTransition, PresentationTransition
from state_machine import StateMachine

presentation = PresentationState("Презентация")
auditory = AuditoryState("Аудитория")
speaker = SpeakerState("Спикер")

presentation.transitions.append(TimeTransition(auditory))
auditory.transitions.extend(
    [TimeTransition(presentation), PresentationTransition(speaker)]
)
speaker.transitions.append(TimeTransition(presentation))

auto_director = StateMachine(presentation)
auto_director.run()
