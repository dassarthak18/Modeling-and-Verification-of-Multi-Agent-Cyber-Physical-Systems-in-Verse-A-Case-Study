from typing import Tuple, List

import numpy as np
from scipy.integrate import ode

from verse import BaseAgent
from verse import LaneMap
from verse.plotter.plotter2D import *
import plotly.graph_objects as go

from enum import Enum, auto
import copy

class TacticalMode(Enum):
    NORMAL = auto()
    ACCEL = auto()
    DECEL = auto()

class State:
    x: float
    y: float
    vx: float
    ax: float
    ''' track mode need not be written explicitly
    as there is only a single track mode '''
    mode:TacticalMode

    def __init__(self, x, y, vx, ax, mode: TacticalMode):
        pass

def decisionLogic(ego:State, others:List[State]):
    output = copy.deepcopy(ego)
    return output

class ACCAgent(BaseAgent):
    
    def __init__(self, id, code=None, file_name=None):
        super().__init__(id, code, file_name)

    @staticmethod
    def dynamic(t, state):
        x, y, vx, ax = state
        x_dot = vx # defines dx/dt
        vx_dot = ax # defines dv/dt=d2x/dt2
        return [x_dot, 0, vx_dot, 0]