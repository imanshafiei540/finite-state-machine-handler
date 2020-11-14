class Input(object):
    """
    This class holds for Input with range value and unit.
    """
    def __init__(self, unit, range_value, going_out_from_super_state=False):
        self.unit = unit
        self.range_value = range_value
        self.going_out_from_super_state = going_out_from_super_state
    
    def get_range_value(self):
        return self.range_value

    def get_going_out_from_super_state(self):
        return self.going_out_from_super_state