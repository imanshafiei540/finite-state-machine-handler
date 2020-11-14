from state_machine.StateMachine import StateMachine
from state_machine.State import State
from state_machine.Input import Input
from state_machine.StateToInput import StateToInput
if __name__ == "__main__":
    t0_state = State(tag="T0", description="Tempreture is under the 25 degree.")
    t1_state = State(tag="T1", description="Tempreture is above the 35 degree.")
    t2_state = State(tag="T2", description="Tempreture is under the 15 degree.")
    states = [t0_state, t1_state, t2_state]
    i0_input = Input(unit="Centigrade", range_value=(35, 100))
    i1_input = Input(unit="Centigrade", range_value=(15, 25))
    i2_input = Input(unit="Centigrade", range_value=(-100, 15))
    i3_input = Input(unit="Centigrade", range_value=(30, 35))
    t0_to_t1 = StateToInput(current_state=t0_state, input_object=i0_input, next_state=t1_state)
    t0_to_t2 = StateToInput(current_state=t0_state, input_object=i2_input, next_state=t2_state)
    t2_to_t0 = StateToInput(current_state=t2_state, input_object=i3_input, next_state=t0_state)
    t1_to_t0 = StateToInput(current_state=t1_state, input_object=i1_input, next_state=t0_state)
    state_to_inputs = [t0_to_t1, t0_to_t2, t2_to_t0, t1_to_t0]
    state_machine_object = StateMachine(states_list=states, input_to_states_list=state_to_inputs)

    while(True):
        input_from_termostat = input("T: ")
        
