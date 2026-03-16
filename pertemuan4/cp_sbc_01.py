import time
from enum import Enum

class TrafficLight(Enum):
    MERAH = "Merah"
    KUNING = "Kuning"
    HIJAU = "Hijau"

state_transitions = {
    TrafficLight.HIJAU: TrafficLight.KUNING,
    TrafficLight.KUNING: TrafficLight.MERAH,
    TrafficLight.MERAH: TrafficLight.HIJAU
}

state_durations = {
    TrafficLight.HIJAU: 5,
    TrafficLight.KUNING: 2,
    TrafficLight.MERAH: 5
}   

def traffic_light_fsm():
    current_state = TrafficLight.HIJAU
    while True:
        print(f"Traffic Light is {current_state.value} - Durasi: {state_durations[current_state]} detik")
        time.sleep(state_durations[current_state])

        current_state = state_transitions[current_state]

if __name__ == "__main__":
    traffic_light_fsm()