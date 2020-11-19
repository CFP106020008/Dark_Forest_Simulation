import numpy as np

def tech_to_control_R(tech):
    # Technology level should be a dimensionless parameter
    # R should be in unit of pc
    control_R = tech*100
    return control_R

