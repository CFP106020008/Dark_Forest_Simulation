import numpy as np
import functions as f


class Civilization:

    def __init__(self, x, y, z, tech, DFA):
        
        self.reset(self, x, y, z, tech, DFA)
        return

    def reset(self, x, y, z, tech, DFA):
        
        self.x     = x
        self.y     = y
        self.z     = z
        self.tech  = tech
        self.control_R = f.tech_to_control_R(self.tech)
        self.observe_R = f.tech_to_observe_R(self.tech)
        self.resource = self.control_R
        self.DFA = DFA #Dark Forest Awareness
        
        # If Hide is true, the civilization would be harder to observe.
        if DFA == True:
            self.Hide = True
        else:
            self.Hide = False

        return







