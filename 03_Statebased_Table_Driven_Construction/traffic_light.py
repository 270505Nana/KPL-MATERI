from enum import enum
import time
#  memanfaatkan enum sebagia state

# automata -> state
class TrafficLightState(enum):
    MERAH = "merah"
    HIJAU = "hijau"
    KUNING = "kuning"


# automata => state atau perubahan atau transisi
state_transition = {
    TrafficLightState.MERAH: TrafficLightState.HIJAU,
    TrafficLightState.HIJAU: TrafficLightState.KUNING,
    TrafficLightState.KUNING: TrafficLightState.MERAH
}

state_durations = {
    TrafficLightState.MERAH:6,
    TrafficLightState.HIJAU:4,
    TrafficLightState.KUNING:1,
}
# map <key, value>
#  key => state awal
#  value => state tujuan

current_state = TrafficLightState.KUNING
next_state = state_transition[current_state]
print(next_state)

current_state = TrafficLightState.MERAH
while true:
    print("Traffic Light: {current_state.value}")
    time.sleep(state_durations[current_state])
    current_state = state_transition[current_state]