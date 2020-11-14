class StateToInput(object):
    """
    This class holds for StateToInput with current state and next state and our input 
    which means we can go to the next state with processing current state and input.
    """
    def __init__(self, current_state, input_object, next_state):
        self.current_state = current_state
        self.input_object = input_object
        self.next_state = next_state

    def get_input_object(self):
        return self.input_object
    
    def get_current_state(self):
        return self.current_state
    
    def get_next_state(self):
        return self.next_state