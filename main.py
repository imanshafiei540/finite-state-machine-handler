from state_machine.StateMachine import StateMachine
from state_machine.State import State
from state_machine.Input import Input
from state_machine.StateToInput import StateToInput

def return_termostat_input(messgae):
    try:
        input_from_termostat = input(messgae)
        float_temp = float(input_from_termostat)
        return float_temp
    except Exception as e:
        print(e)
        return 0
    
if __name__ == "__main__":
    t0_state = State(tag="T0", description="HEAT: OFF and COOL: OFF; Tempreture is under the 25 degree.")
    t1_state = State(tag="T1", description="HEAT: OFF and COOL: ON; Tempreture is above the 35 degree.", is_super_state=True)
    t2_state = State(tag="T2", description="HEAT: ON and COOL: OFF; Tempreture is under the 15 degree.")
    states = [t0_state, t1_state, t2_state]
    i0_input = Input(unit="Centigrade", range_value=(35, 100))
    i1_input = Input(unit="Centigrade", range_value=(15, 25))
    i2_input = Input(unit="Centigrade", range_value=(-100, 15))
    i3_input = Input(unit="Centigrade", range_value=(30, 35), going_out_from_super_state=True)
    t0_to_t1 = StateToInput(current_state=t0_state, input_object=i0_input, next_state=t1_state)
    t0_to_t2 = StateToInput(current_state=t0_state, input_object=i2_input, next_state=t2_state)
    t2_to_t0 = StateToInput(current_state=t2_state, input_object=i3_input, next_state=t0_state)
    t1_to_t0 = StateToInput(current_state=t1_state, input_object=i1_input, next_state=t0_state)
    state_to_inputs = [t0_to_t1, t0_to_t2, t2_to_t0, t1_to_t0]
    state_machine_object = StateMachine(states_list=states, input_to_states_list=state_to_inputs)


    s0_state = State(tag="S0", description="Tempreture is above 35 degree and CRS is 4RPS")
    s1_state = State(tag="S1", description="Tempreture is above 40 degree and CRS is 6RPS")
    s2_state = State(tag="S2", description="Tempreture is above 45 degree and CRS is 8RPS")
    super_state_states = [s0_state, s1_state, s2_state]
    super_i0_input = Input(unit="Centigrade", range_value=(35, 40))
    super_i1_input = Input(unit="Centigrade", range_value=(40, 45))
    super_i2_input = Input(unit="Centigrade", range_value=(45, 100))
    s0_to_s1 = StateToInput(current_state=s0_state, input_object=super_i1_input, next_state=s1_state)
    s1_to_s2 = StateToInput(current_state=s1_state, input_object=super_i2_input, next_state=s2_state)
    s1_to_s0 = StateToInput(current_state=s1_state, input_object=i3_input, next_state=s0_state)
    s2_to_s1 = StateToInput(current_state=s2_state, input_object=super_i0_input, next_state=s1_state)
    super_states_to_input = [s0_to_s1, s1_to_s2, s1_to_s0, s2_to_s1]
    super_state_machine_object = StateMachine(states_list=super_state_states, input_to_states_list=super_states_to_input)

    next_state = ""
    current_state = t0_state
    while(True):
        if current_state:
            print(f'Current state: {current_state.get_tag()} Description: {current_state.get_description()}')
        input_from_termostat = return_termostat_input("T: ")
        for input_to_state in state_machine_object.get_input_to_states():
            temperture = input_to_state.get_input_object().get_range_value()
            input_to_state_current_state = input_to_state.get_current_state()
            min_temp = temperture[0]
            max_temp = temperture[1]
            if  (min_temp <= input_from_termostat < max_temp) and (input_to_state_current_state.get_tag() == current_state.get_tag()):
                next_state = input_to_state.get_next_state()
                if next_state.is_super_state:
                    next_state_super_state = ""
                    current_state_super_state = s0_state
                    out_from_super_state = False
                    while(not out_from_super_state):
                        print(f'SUPER STATE: Current state: {current_state_super_state.get_tag()} Description: {current_state_super_state.get_description()}')
                        input_from_termostat = return_termostat_input("(SUPER STATE)T: ")
                        for input_to_state_in_super_state in super_state_machine_object.get_input_to_states():
                            temperture = input_to_state_in_super_state.get_input_object().get_range_value()
                            input_to_state_current_state = input_to_state_in_super_state.get_current_state()
                            min_temp = temperture[0]
                            max_temp = temperture[1]
                            if  (min_temp <= input_from_termostat < max_temp) and (input_to_state_current_state.get_tag() == current_state_super_state.get_tag()):
                                next_state_super_state = input_to_state_in_super_state.get_next_state()
                                if input_to_state_in_super_state.get_input_object().get_going_out_from_super_state():
                                    out_from_super_state = True
                                break
                        current_state_super_state = next_state_super_state
                break
        
        current_state = next_state
