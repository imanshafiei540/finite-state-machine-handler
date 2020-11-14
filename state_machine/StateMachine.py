class StateMachine(object):
    """
    This class holds for StateMachine with list of states and list of input to states.
    """
    def __init__(self, states_list, input_to_states_list):
        self.states = states_list
        self.input_to_states = input_to_states_list