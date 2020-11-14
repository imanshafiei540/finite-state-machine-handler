class State(object):
    """
    This class holds for State.
    """
    def __init__(self, tag, description, is_super_state=False):
        self.tag = tag
        self.description = description
        self.is_super_state = is_super_state
    
    def get_tag(self):
        return self.tag
    
    def get_description(self):
        return self.description
    
    def get_is_super_state(self):
        return self.is_super_state